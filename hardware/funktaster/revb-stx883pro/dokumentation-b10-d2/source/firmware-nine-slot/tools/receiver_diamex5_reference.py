"""Pure EV1527 and Dalum/DIAMEX ATtiny fixed-code receive helpers."""
from __future__ import annotations

import hashlib
import binascii
import statistics
from collections import deque


PULSE_US = 320
MIN_FIXED_CODE = 0x100000
MAX_FIXED_CODE = 0xFFFFFF
DIAMEX_PROTOCOL = "Dalum-DIAMEX"
DIAMEX_V2_PROTOCOL = "Dalum-DIAMEX2"
# Actual generated preamble pair including GPIO/loop instructions, not just
# the two _delay_us(150) calls. The firmware build verifies this cycle count.
DIAMEX_V2_PREAMBLE_PAIR_CYCLES = 2887


class EdgePolarityFilter:
    """Ignore duplicate GPIO notifications, not genuine short RF pulses.

    Preserve the first edge timestamp. Consecutive rising (or falling)
    notifications cannot both describe a transition of the same input.
    A kernel sequence gap invalidates that inference: never bridge a lost edge.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.level = None
        self.sequence = None

    def accept(self, level: bool, sequence: int) -> bool:
        if self.sequence is not None and sequence != self.sequence + 1:
            self.level = None
        self.sequence = sequence
        if level == self.level:
            return False
        self.level = level
        return True


def diamex_v2_packet(identifier: int, event: int, repeat: int, age_ticks: int) -> bytes:
    """Shared software model of the bounded ATtiny v2 on-air packet."""
    if not 1 <= identifier <= 255 or not 0 <= event <= 255 or not 0 <= repeat < 5 or not 0 <= age_ticks <= 30000:
        raise ValueError('Ungültiges DIAMEX2-Telegramm')
    data = bytes((0xD3, 0x6D, identifier, event, repeat)) + age_ticks.to_bytes(2, 'big')
    return data + binascii.crc_hqx(data, 0).to_bytes(2, 'big')


def diamex_code(identifier: int) -> str:
    data = bytes((0xD3, 0x6C, identifier))
    return (data + bytes((diamex_crc8(data),))).hex().upper()


def diamex_crc8(data: bytes) -> int:
    crc = 0
    for value in data:
        crc ^= value
        for _ in range(8):
            crc = ((crc << 1) ^ (0x07 if crc & 0x80 else 0)) & 0xFF
    return crc


def _diamex_timing(header: list[int]) -> tuple[float, float] | None:
    # At least four recovered preamble cycles; a receiver may miss the first
    # edges while its AGC settles. Require sync, payload magic and CRC as well.
    if len(header) < 10:
        return None
    preamble = header[-10:-2]
    pairs = list(zip(preamble[0::2], preamble[1::2]))
    unit = statistics.median(high + low for high, low in pairs) / 3
    if not 70 <= unit <= 140:
        return None
    # The CC1101's asynchronous slicer can shift every falling edge by tens
    # of microseconds without changing a high/low pair's total duration.
    # Recover that duty-cycle bias from the balanced preamble instead of
    # rejecting a valid, CRC-protected telegram as malformed.
    bias = statistics.median((low - high) / 2 for high, low in pairs)
    if abs(bias) > 0.7 * unit:
        return None
    if not all(
        1.1 <= (high + bias) / unit <= 1.9
        and 1.1 <= (low - bias) / unit <= 1.9
        and 2.5 <= (high + low) / unit <= 3.5
        for high, low in pairs
    ):
        return None
    if not 2.4 <= (header[-2] + bias) / unit <= 3.6 or not 7.2 <= (header[-1] - bias) / unit <= 10.8:
        return None
    return unit, bias


def _diamex_payload_bias(pulses: list[float], unit: float, bias: float) -> float:
    """Bounded slicer calibration from the 15 shared, known D3 6C/6D bits.

    RF settling may move the falling edge between preamble and payload. Fit
    only the known prefix, never guess data/CRC bits or widen pulse windows.
    The final magic bit differs between V1 and V2 and is deliberately omitted.
    """
    if len(pulses) < 30:
        return bias
    offsets = []
    known = f'{0xD36C:016b}'[:15]
    for index, bit in enumerate(known):
        high = unit * (2 if bit == '1' else 1)
        offsets.extend((high - pulses[2 * index], pulses[2 * index + 1] - (3 * unit - high)))
    fitted = statistics.median(offsets)
    if abs(fitted - bias) > .25 * unit:
        return bias
    for index, bit in enumerate(known):
        high = (pulses[2 * index] + fitted) / unit
        low = (pulses[2 * index + 1] - fitted) / unit
        if not ((1.65 <= high <= 2.35 and .65 <= low <= 1.35) if bit == '1'
                else (.65 <= high <= 1.35 and 1.65 <= low <= 2.35)):
            return bias
    return fitted


def _diamex_bytes(pulses: list[int], unit: float, bias: float = 0) -> bytes | None:
    # Decode at the final falling edge. The last LOW has no ending edge when
    # the ATtiny sleeps, and merges with the 3-ms pause between repetitions.
    # Only that final LOW is omitted; all previous high/low pairs are checked.
    if len(pulses) not in {63, 143}:
        return None
    bits = (len(pulses) + 1) // 2
    value = 0
    for bit in range(bits):
        high = (pulses[bit * 2] + bias) / unit
        if 0.65 <= high <= 1.35:
            one = 0
        elif 1.65 <= high <= 2.35:
            one = 1
        else:
            return None
        if bit < bits - 1:
            low = (pulses[bit * 2 + 1] - bias) / unit
            if not ((1.65 <= low <= 2.35) if not one else (0.65 <= low <= 1.35)):
                return None
            if not 2.4 <= high + low <= 3.6:
                return None
        value = (value << 1) | one
    return value.to_bytes(bits // 8, "big")


def _diamex_payload(pulses: list[int], unit: float, bias: float = 0) -> str | None:
    frame = _diamex_bytes(pulses, unit, bias)
    if frame is None or len(frame) != 4:
        return None
    if frame[:2] != b"\xd3\x6c" or not 1 <= frame[2] <= 5:
        return None
    if diamex_crc8(frame[:3]) != frame[3]:
        return None
    return frame.hex().upper()


class DiamexStreamDecoder:
    """Bounded edge decoder. Recognized corrupt frames must not use fallback."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.header: deque[int] = deque(maxlen=18)
        self.payload: list[int] | None = None
        self.unit = 100.0
        self.bias = 0.0
        self.recognized = False
        self.last_event = None
        self.last_packet = None

    def feed(self, duration_us: float) -> str | None:
        if duration_us <= 0 or duration_us >= 8_000:
            self.reset()
            return None
        if self.payload is not None:
            self.payload.append(duration_us)
            if len(self.payload) == 63:
                self.bias = _diamex_payload_bias(self.payload, self.unit, self.bias)
                prefix = _diamex_bytes(self.payload, self.unit, self.bias)
                if prefix is not None and prefix[:2] == b'\xd3\x6d':
                    return None  # v2 has 72 payload bits, not 32
                result = _diamex_payload(self.payload, self.unit, self.bias)
                self.last_packet = bytes.fromhex(result) if result else None
                self.last_event = None
                self.payload = None
                self.header.clear()
                return result
            if len(self.payload) == 143:
                frame = _diamex_bytes(self.payload, self.unit, self.bias)
                self.last_event = None
                result = None
                if (frame is not None and frame[:2] == b'\xd3\x6d' and frame[2] > 0
                        and frame[4] < 5 and int.from_bytes(frame[5:7], 'big') <= 30000
                        and binascii.crc_hqx(frame[:-2], 0) == int.from_bytes(frame[-2:], 'big')):
                    # Recover nominal timer rate from the balanced preamble.
                    # Include the actually observed payload, excluding only the
                    # final low. Timestamp refers to firmware boot, not wall time.
                    nominal_unit = DIAMEX_V2_PREAMBLE_PAIR_CYCLES / (3 * 9.6)
                    age = int.from_bytes(frame[5:7], 'big') * (256 / 9.6) * self.unit / nominal_unit
                    self.last_event = {'event_id': frame[3], 'repeat': frame[4],
                                       'offset_us': age + 36 * self.unit + sum(self.payload)}
                    self.last_packet = frame
                    result = diamex_code(frame[2])
                self.payload = None
                self.header.clear()
                return result
        self.header.append(duration_us)
        # Also recover at the next valid preamble after an incomplete frame.
        if duration_us >= 500:
            timing = _diamex_timing(list(self.header))
            if timing is not None:
                self.recognized = True
                self.unit, self.bias = timing
                self.payload = []
                self.header.clear()
        return None


def decode_received_frame(durations_us: list[int]) -> tuple[str | None, str]:
    """Protocol priority is important: never fingerprint a bad DIAMEX CRC."""
    decoder = DiamexStreamDecoder()
    recognized = False
    for duration in durations_us:
        code = decoder.feed(duration)
        recognized = recognized or decoder.recognized
        if code:
            return code, DIAMEX_V2_PROTOCOL if decoder.last_event else DIAMEX_PROTOCOL
    if recognized:
        return None, DIAMEX_PROTOCOL
    code = decode_ev1527(durations_us)
    if code:
        return code, "EV1527"
    return adaptive_fingerprint(durations_us), "Festcode-Fingerprint"


def normalise_fixed_code(code: str) -> str:
    value = int(code, 16)
    if value < MIN_FIXED_CODE or value > MAX_FIXED_CODE:
        raise ValueError("Der Festcode muss genau 24 Bit umfassen")
    return f"{value:06X}"


def ev1527_pulses(code: str, pulse_us: int = PULSE_US) -> list[tuple[int, int]]:
    """Return one EV1527/OOK frame as (GPIO level, duration in microseconds)."""
    fixed = normalise_fixed_code(code)
    bits = f"{int(fixed, 16):024b}"
    pulses: list[tuple[int, int]] = [(1, pulse_us), (0, pulse_us * 31)]
    for bit in bits:
        pulses.extend(((1, pulse_us * (3 if bit == "1" else 1)), (0, pulse_us * (1 if bit == "1" else 3))))
    return pulses


def decode_ev1527(durations_us: list[int]) -> str | None:
    """Decode alternating high/low durations, tolerating a leading half pulse."""
    pulses = [value for value in durations_us if 70 <= value <= 12_000]
    for offset in (0, 1):
        candidate = pulses[offset:]
        # Locate and skip a long EV1527 sync gap when it is included.
        if len(candidate) >= 50 and candidate[1] > 5_000:
            candidate = candidate[2:]
        if len(candidate) < 48:
            continue
        candidate = candidate[:48]
        bits: list[str] = []
        for high, low in zip(candidate[0::2], candidate[1::2]):
            ratio = high / max(low, 1)
            if ratio <= 0.55:
                bits.append("0")
            elif ratio >= 1.8:
                bits.append("1")
            else:
                break
        if len(bits) == 24:
            return f"{int(''.join(bits), 2):06X}"
    return None


def adaptive_fingerprint(durations_us: list[int]) -> str | None:
    """Stable fallback for unknown fixed-code pulse formats."""
    pulses = [value for value in durations_us if 70 <= value <= 12_000]
    if len(pulses) < 24:
        return None
    low, high = min(pulses), max(pulses)
    for _ in range(10):
        threshold = (low + high) / 2
        short = [value for value in pulses if value <= threshold]
        long = [value for value in pulses if value > threshold]
        if not short or not long:
            return None
        low, high = statistics.median(short), statistics.median(long)
    bits = "".join("0" if value <= (low + high) / 2 else "1" for value in pulses)
    return hashlib.sha256(f"{len(bits)}:{bits}".encode("ascii")).hexdigest().upper()[:32]
