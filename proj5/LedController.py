import time
import RPi.GPIO as GPIO
from threading import Thread

lightpins = [18, 23, 24]
lights = [[1, -1, 0], [0, 1, -1], [-1, 1, 0],
          [0, -1, 1], [1, 0, -1], [-1, 0, 1]]


class LedController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self._active_led = None

    def _led_on(self, which):
        pattern = lights[which]
        for n in range(3):
            if pattern[n] == -1:
                GPIO.setup(lightpins[n], GPIO.OUT)
                GPIO.output(lightpins[n], GPIO.LOW)
            elif pattern[n] == 1:
                GPIO.setup(lightpins[n], GPIO.OUT)
                GPIO.output(lightpins[n], GPIO.HIGH)

    def _led_off(self):
        for n in range(3):
            GPIO.setup(lightpins[n], GPIO.IN)

    def _hold_led(self, which, duration):
        self._led_on(which)
        time.sleep(duration)
        self._led_off()

    def _resume_state(self):
        if self._active_led is not None:
            self._led_on(self._active_led)
        else:
            self._led_off()

    def twinkle_all_leds(self, times, duration):
        for _ in range(times):
            for n in range(6):
                self._hold_led(n, duration / 6)
        self._resume_state()

    def power_up_leds(self, duration):
        for _ in range(3):
            for n in range(6):
                if n < 3:
                    self._hold_led(n * 2, duration / 18)
                else:
                    self._hold_led(n * 2 - 5, duration / 18)
        self._resume_state()

    def power_down_leds(self, duration):
        for _ in range(2):
            for n in range(6):
                if n < 3:
                    self._hold_led((5 - n) * 2 - 5, duration / 18)
                else:
                    self._hold_led((5 - n) * 2, duration / 18)
        self._resume_state()
        self._active_led = None

    def set_led_duration(self, led_id, duration):
        if (led_id >= len(lights)):
            return
        self._active_led = led_id
        self._led_on(led_id)
        t1 = Thread(target=lambda: self._turn_off_led_after(duration))
        t1.start()

    def _turn_off_led_after(self, duration):
        time.sleep(duration)
        self._led_off()
        self._active_led = None
