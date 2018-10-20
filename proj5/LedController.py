import time
import RPi.GPIO as GPIO

lightpins = [18, 23, 24]
lights = [[1, -1, 0], [0, 1, -1], [-1, 1, 0],
          [0, -1, 1], [1, 0, -1], [-1, 0, 1]]


class LedController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def led_on(self, which):
        pattern = lights[which]
        for n in range(3):
            if pattern[n] == -1:
                GPIO.setup(lightpins[n], GPIO.OUT)
                GPIO.output(lightpins[n], GPIO.LOW)
            elif pattern[n] == 1:
                GPIO.setup(lightpins[n], GPIO.OUT)
                GPIO.output(lightpins[n], GPIO.HIGH)

    def led_off(self):
        for n in range(3):
            GPIO.setup(lightpins[n], GPIO.IN)

    def hold_led(self, which, duration):
        self.led_on(which)
        time.sleep(duration)
        self.led_off()

    def twinkle_all_leds(self, duration):
        for n in range(6):
            self.hold_led(n, duration)

    def power_up_leds(self, duration):
        for n in range(6):
            self.hold_led((n * 2) % 5, duration)

    def power_down_leds(self, duration):
        for n in range(6):
            self.light_led(((5 - n) * 2) % 5, duration)
