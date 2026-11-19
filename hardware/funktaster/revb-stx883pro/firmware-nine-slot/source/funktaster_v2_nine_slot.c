/* Dalum DIAMEX v2, ATtiny13A, PB3 -> STX882, 9.6 MHz / HFUSE FB LFUSE 76.
 * 9-byte packet: D3 6D ID EVENT REPEAT AGE_H AGE_L CRC16_H CRC16_L.
 * AGE: Timer0 /256 ticks since firmware startup, captured before preamble.
 * No interrupts during pulse generation. Timer overflow is polled at least
 * every byte (2.4 ms), EEPROM byte (3.4 ms), or busy-wait iteration.
 * Not an acknowledged link. Physical RF acceptance is required before use.
 */
#define F_CPU 9600000UL
#include <avr/io.h>
#include <avr/eeprom.h>
#include <avr/sleep.h>
#include <util/delay.h>
#include <stdint.h>
#ifndef BUTTON_ID
#define BUTTON_ID 1
#endif
#if BUTTON_ID < 1 || BUTTON_ID > 9
#error "Nine-slot firmware requires BUTTON_ID 1..9"
#endif

static uint8_t high_ticks;

static uint16_t ticks(void) {
    uint8_t low = TCNT0;
    if (TIFR0 & _BV(TOV0)) {
        TIFR0 = _BV(TOV0);
        ++high_ticks;
        low = TCNT0;
    }
    return ((uint16_t)high_ticks << 8) | low;
}

static void wait_until(uint16_t target) {
    while (ticks() < target) { }
}

static uint8_t next_event(void) {
    /* 32 wear-levelled records (sequence, complement), all 64 EEPROM bytes.
     * A power cut during writing leaves the old valid records available.
     * Both bytes finish before the first packet; no counter write per repeat.
     */
    uint8_t latest = 255, slot = 31, found = 0;
    for (uint8_t i = 0; i < 32; ++i) {
        uint8_t a = eeprom_read_byte((uint8_t *)(uint16_t)(i * 2));
        uint8_t b = eeprom_read_byte((uint8_t *)(uint16_t)(i * 2 + 1));
        if ((uint8_t)(a ^ b) == 255 && (!found || (int8_t)(a - latest) > 0)) {
            latest = a; slot = i; found = 1;
        }
        ticks();
    }
    ++latest;
    slot = (slot + 1) & 31;
    eeprom_update_byte((uint8_t *)(uint16_t)(slot * 2), latest);
    while (!eeprom_is_ready()) ticks();
    eeprom_update_byte((uint8_t *)(uint16_t)(slot * 2 + 1), (uint8_t)~latest);
    while (!eeprom_is_ready()) ticks();
    return latest;
}

static uint16_t crc_add(uint16_t crc, uint8_t data) {
    crc ^= (uint16_t)data << 8;
    for (uint8_t i = 0; i < 8; ++i)
        crc = (crc << 1) ^ ((crc & 0x8000) ? 0x1021 : 0);
    return crc;
}

static void send_byte(uint8_t data) {
    for (uint8_t i = 0; i < 8; ++i) {
        if (data & 128) {
            PORTB |= _BV(PB3); _delay_us(200);
            PORTB &= ~_BV(PB3); _delay_us(100);
        } else {
            PORTB |= _BV(PB3); _delay_us(100);
            PORTB &= ~_BV(PB3); _delay_us(200);
        }
        data <<= 1;
    }
    ticks();
}

static void send_frame(uint8_t event, uint8_t repeat) {
    uint16_t age = ticks();
    uint8_t data[9] = {0xD3, 0x6D, BUTTON_ID, event, repeat,
                       (uint8_t)(age >> 8), (uint8_t)age, 0, 0};
    uint16_t crc = 0;
    for (uint8_t i = 0; i < 7; ++i) crc = crc_add(crc, data[i]);
    data[7] = crc >> 8; data[8] = crc;
    for (uint8_t i = 0; i < 8; ++i) {
        PORTB |= _BV(PB3); _delay_us(150);
        PORTB &= ~_BV(PB3); _delay_us(150);
    }
    PORTB |= _BV(PB3); _delay_us(300);
    PORTB &= ~_BV(PB3); _delay_us(900);
    for (uint8_t i = 0; i < 9; ++i) send_byte(data[i]);
}

int main(void) {
    PORTB &= ~_BV(PB3); DDRB |= _BV(PB3);
    TCCR0B = _BV(CS02);  /* Timer /256, one tick = 26 2/3 us nominal */
    uint8_t event = next_event();
    wait_until(563);   /* 15.01 ms, includes EEPROM write / supply settle */
    send_frame(event, 0);
    /* Rev B nine-slot schedule, on-air V2 format unchanged.
     * Three complete 9-slot rounds fit inside the existing 1000-ms hold.
     * Multipliers 1,2,4 are coprime to 9: each round is a permutation.
     * First packet remains immediate after settle. No extra random delay.
     * End <= ~773 ms nominal, <= ~967 ms at 1.25 time scaling.
     * Clock skew / asynchronous presses can still collide; no ACK exists.
     */
    for (uint8_t repeat = 1; repeat < 4; ++repeat) {
        uint8_t slot = ((BUTTON_ID - 1) * (1U << (repeat - 1))) % 9;
        uint16_t milliseconds = 45 + (uint16_t)(repeat - 1) * 243 + slot * 27;
        wait_until((milliseconds * 75U) / 2U);
        send_frame(event, repeat);
    }
    PORTB &= ~_BV(PB3);
    TCCR0B = 0;
    ADCSRA &= ~_BV(ADEN); ACSR |= _BV(ACD);
    set_sleep_mode(SLEEP_MODE_PWR_DOWN); sleep_enable();
    for (;;) sleep_cpu();
}
