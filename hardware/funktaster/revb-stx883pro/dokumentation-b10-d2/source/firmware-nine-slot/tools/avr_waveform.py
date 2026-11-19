"""Small fail-closed instruction model for *these* compiled ATtiny images.

Not a general AVR emulator or RF/hardware acceptance. Models the compiler's
instructions, cycle counts, stack, Timer0 /256 and EEPROM write completion to
derive PB3 edges from the actual disassembly, not from the C timing constants.
Unknown instructions/peripheral modes are errors, never silently skipped.
"""
import re


class AVR:
    def __init__(self, listing, eeprom=None):
        self.program = {}
        for line in listing.splitlines():
            match = re.match(r'\s*([0-9a-f]+):\s+((?:[0-9a-f]{2} )+)\s*(\w+)\s*(.*)', line)
            if match:
                address, raw, op, rest = match.groups()
                args = [x.strip() for x in rest.split(';')[0].split(',') if x.strip()]
                target = re.search(r';\s*0x([0-9a-f]+)', rest)
                self.program[int(address, 16)] = (op, args, len(raw.split()), int(target[1], 16) if target else None)
        self.ram = bytearray(256)
        self.eeprom = bytearray(eeprom if eeprom is not None else b'\xff' * 64)
        self.pc = self.cycles = 0
        self.flags = 0
        self.timer_start = None
        self.timer_count = 0
        self.pending_write = None
        self.edges = []
        self.min_sp = 159
        self.instructions = 0
        self.slept = False

    def update(self):
        if self.timer_start is not None:
            count = (self.cycles - self.timer_start) // 256
            if count // 256 > self.timer_count // 256:
                self.ram[0x58] |= 2
            self.timer_count = count
        if self.pending_write and self.cycles >= self.pending_write[0]:
            _, address, value = self.pending_write
            self.eeprom[address] = value
            self.pending_write = None
            self.ram[0x3c] &= ~2

    def read(self, address):
        self.update()
        if address == 0x52:
            return self.timer_count & 255
        if address == 0x5f:
            return self.flags
        return self.ram[address]

    def write(self, address, value):
        value &= 255
        old = self.ram[address]
        if address == 0x58:
            self.ram[address] &= ~value
            return
        if address == 0x53:
            if value not in (0, 4):
                raise AssertionError('Unexpected timer mode')
            self.timer_start = self.cycles if value else None
            self.timer_count = 0
        if address == 0x5f:
            self.flags = value
        if address == 0x3c:
            if value & 1:
                self.ram[0x3d] = self.eeprom[self.ram[0x3e] & 63]
                value &= ~1
            if value & 2 and not old & 2:
                assert value & 4, 'EEPROM write without master enable'
                self.pending_write = (self.cycles + 32640, self.ram[0x3e] & 63, self.ram[0x3d])
        self.ram[address] = value
        if address == 0x38 and (value ^ old) & 8:
            self.edges.append((self.cycles / 9.6, 1 if value & 8 else 0))
        if address == 0x5d:
            self.min_sp = min(self.min_sp, value)
            assert value >= 0x61, 'Stack collided with static storage'

    def register(self, name):
        return int(name.removeprefix('r'))

    def push(self, value):
        sp = self.ram[0x5d]
        self.ram[sp] = value & 255
        self.write(0x5d, sp - 1)

    def pop(self):
        self.write(0x5d, self.ram[0x5d] + 1)
        return self.ram[self.ram[0x5d]]

    def arithmetic(self, a, b, carry, subtract, chained=False):
        previous_zero = bool(self.flags & 2)
        total = a - b - carry if subtract else a + b + carry
        result = total & 255
        c = total < 0 if subtract else total > 255
        n = bool(result & 128)
        v = bool(((a ^ b) if subtract else ~(a ^ b)) & (a ^ result) & 128)
        z = result == 0 and (previous_zero if chained else True)
        self.flags = (self.flags & ~31) | int(c) | (int(z) << 1) | (int(n) << 2) | (int(v) << 3) | (int(n != v) << 4)
        return result

    def run(self, max_cycles=10_000_000, stop_after_edges=None):
        while self.cycles < max_cycles:
            self.update()
            op, args, width, target = self.program[self.pc]
            next_pc, cost = self.pc + width, 1
            reg = lambda i: self.register(args[i])
            value = lambda i: self.ram[reg(i)]
            imm = lambda i: int(args[i], 0)
            if op == 'ldi': self.ram[reg(0)] = imm(1)
            elif op == 'mov': self.ram[reg(0)] = value(1)
            elif op == 'movw': self.ram[reg(0):reg(0)+2] = self.ram[reg(1):reg(1)+2]
            elif op in {'add', 'adc', 'sub', 'sbc', 'cp', 'cpc', 'cpi', 'subi', 'sbci'}:
                a = value(0)
                b = imm(1) if op in {'cpi', 'subi', 'sbci'} else value(1)
                carry = self.flags & 1 if op in {'adc', 'sbc', 'sbci', 'cpc'} else 0
                result = self.arithmetic(a, b, carry, op not in {'add', 'adc'}, op in {'sbc', 'sbci', 'cpc'})
                if op not in {'cp', 'cpc', 'cpi'}: self.ram[reg(0)] = result
            elif op in {'andi', 'ori', 'and', 'eor', 'com'}:
                a = value(0)
                b = imm(1) if op in {'andi', 'ori'} else (value(1) if op != 'com' else 255)
                result = (a & b) if op in {'andi', 'and'} else (a | b) if op == 'ori' else (a ^ b)
                self.ram[reg(0)] = result
                self.flags = (self.flags & ~30) | ((result == 0) << 1) | ((bool(result & 128)) << 2) | ((bool(result & 128)) << 4)
                if op == 'com': self.flags |= 1
            elif op in {'inc', 'dec'}:
                result = (value(0) + (1 if op == 'inc' else -1)) & 255
                n = bool(result & 128); v = result == (128 if op == 'inc' else 127)
                self.ram[reg(0)] = result
                self.flags = (self.flags & ~30) | ((result == 0) << 1) | (n << 2) | (v << 3) | ((n != v) << 4)
            elif op in {'lsr', 'asr', 'ror', 'swap'}:
                a = value(0)
                if op == 'swap': self.ram[reg(0)] = ((a << 4) | (a >> 4)) & 255
                else:
                    result = (a >> 1) | ((self.flags & 1) << 7 if op == 'ror' else (a & 128) if op == 'asr' else 0)
                    c = bool(a & 1); n = bool(result & 128); v = n != c
                    self.ram[reg(0)] = result
                    self.flags = (self.flags & ~31) | c | ((result == 0) << 1) | (n << 2) | (v << 3) | ((n != v) << 4)
            elif op in {'adiw', 'sbiw'}:
                low = reg(0); old = self.ram[low] | self.ram[low+1] << 8
                result = (old + (imm(1) if op == 'adiw' else -imm(1))) & 65535
                n = bool(result & 32768)
                v = (not bool(old & 32768) and n) if op == 'adiw' else (bool(old & 32768) and not n)
                c = (bool(old & 32768) and not n) if op == 'adiw' else (not bool(old & 32768) and n)
                self.flags = (self.flags & ~31) | int(c) | ((result == 0) << 1) | (n << 2) | (v << 3) | ((n != v) << 4)
                self.ram[low], self.ram[low+1] = result & 255, result >> 8; cost = 2
            elif op == 'in': self.ram[reg(0)] = self.read(imm(1) + 32)
            elif op == 'out': self.write(imm(0) + 32, value(1))
            elif op == 'lds': self.ram[reg(0)] = self.read(imm(1)); cost = 2
            elif op == 'sts': self.write(imm(0), value(1)); cost = 2
            elif op in {'sbi', 'cbi'}:
                address, bit = imm(0) + 32, imm(1)
                self.write(address, (self.read(address) | (1 << bit)) if op == 'sbi' else (self.read(address) & ~(1 << bit))); cost = 2
            elif op in {'ld', 'st', 'std'}:
                pointer = args[1] if op == 'ld' else args[0]
                low = {'X':26, 'Y':28, 'Z':30}[pointer[0]]
                address = self.ram[low] | self.ram[low+1] << 8
                if '+' in pointer and not pointer.endswith('+'): address += int(pointer.split('+')[1])
                if op == 'ld': self.ram[reg(0)] = self.read(address)
                else: self.write(address, value(1))
                if pointer.endswith('+'):
                    address += 1; self.ram[low], self.ram[low+1] = address & 255, address >> 8
                cost = 2
            elif op == 'push': self.push(value(0)); cost = 2
            elif op == 'pop': self.ram[reg(0)] = self.pop(); cost = 2
            elif op == 'rcall':
                self.push((next_pc // 2) & 255); self.push((next_pc // 2) >> 8)
                next_pc, cost = target, 3
            elif op == 'ret': next_pc = (self.pop() << 8 | self.pop()) * 2; cost = 4
            elif op == 'rjmp': next_pc, cost = target, 2
            elif op in {'brne', 'breq', 'brcs', 'brcc', 'brge', 'brlt', 'brtc', 'brts', 'brmi', 'brpl'}:
                condition = {'brne': not bool(self.flags & 2), 'breq': bool(self.flags & 2),
                             'brcs': bool(self.flags & 1), 'brcc': not bool(self.flags & 1),
                             'brge': not bool(self.flags & 16), 'brlt': bool(self.flags & 16),
                             'brtc': not bool(self.flags & 64), 'brts': bool(self.flags & 64),
                             'brmi': bool(self.flags & 4), 'brpl': not bool(self.flags & 4)}[op]
                if condition: next_pc, cost = target, 2
            elif op in {'sbrs', 'sbrc', 'sbic'}:
                bit_set = bool((self.read(imm(0)+32) if op == 'sbic' else value(0)) & (1 << imm(1)))
                if bit_set == (op == 'sbrs'):
                    skip = self.program[next_pc][2]; next_pc += skip; cost += skip // 2
            elif op == 'cli': self.flags &= ~128
            elif op == 'bst': self.flags = (self.flags & ~64) | (bool(value(0) & (1 << imm(1))) << 6)
            elif op == 'bld': self.ram[reg(0)] = (value(0) & ~(1 << imm(1))) | (bool(self.flags & 64) << imm(1))
            elif op == 'sleep': self.slept = True; break
            elif op != 'nop': raise AssertionError(f'Unsupported instruction {op} at {self.pc:x}')
            assert next_pc is not None
            self.pc = next_pc; self.cycles += cost; self.instructions += 1
            if stop_after_edges and len(self.edges) >= stop_after_edges: break
        else:
            raise AssertionError('Firmware exceeded bounded execution window')
        return self
