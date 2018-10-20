import time
import RPi.GPIO as GPIO

lightpins = [18, 23, 24]
lights = [[1, -1, 0], [-1, 1, 0], [0, 1, -1], [0, -1, 1], [1, 0, -1], [-1, 0, 1]]


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)


def light_led(which, duration):
    pattern = lights[which]
    for n in range(3):
        if pattern[n] == -1:
            GPIO.setup(lightpins[n], GPIO.OUT)
            GPIO.output(lightpins[n], GPIO.LOW)
        elif pattern[n] == 1:
            GPIO.setup(lightpins[n], GPIO.OUT)
            GPIO.output(lightpins[n], GPIO.HIGH)
    time.sleep(duration)
    for n in range(3):
        GPIO.setup(lightpins[n], GPIO.IN)


def twinkle_all_leds(duration):
    for n in range(6):
        light_led(n, duration)


def power_up_leds(duration):
    for n in range(6):
        light_led((n * 2) % 5, duration)


def power_down_leds(duration):
    for n in range(6):
        light_led(((5 - n) * 2) % 5, duration)


setup()
while True:
    light_led(0, 1000)