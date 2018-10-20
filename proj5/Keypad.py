import RPi.GPIO as GPIO
import time
from LedController import LedController


class Keypad():
    def __init__(self):
        # rowpins: contains all the pins connected to the board,
        #          corresponding to each row
        # columnpins: same, but with columns
        # dict:
        #   key (tuple(int, int)):  (rowpin, columnpin)
        #   value (string):         value of the button on keypad
        self._led_controller = LedController()
        self._rowpins = [26, 19, 13, 6]
        self._columnpins = [5, 21, 20]
        self._dict = {}
        for i in range(len(self._rowpins)):
            for j in range(len(self._columnpins)):
                if i == 3:
                    if j == 0:
                        self._dict[(self._rowpins[i],
                                    self._columnpins[j])] = "*"
                    elif j == 1:
                        self._dict[(self._rowpins[i],
                                    self._columnpins[j])] = "0"
                    else:
                        self._dict[(self._rowpins[i],
                                    self._columnpins[j])] = "#"
                else:
                    self._dict[(self._rowpins[i], self._columnpins[j])
                               ] = str(1+3*i+j)

        # initializes the row and column pins
        GPIO.setmode(GPIO.BCM)
        for rp in self._rowpins:
            GPIO.setup(rp, GPIO.OUT)
        for cp in self._columnpins:
            GPIO.setup(cp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def _get_input_if_any(self):
        key = self._do_polling()
        if key is not None:
            return self._dict[key]
        else:
            return None

    # checks if any button is pressed
    # returns the location (row-pin, column-pin) as the one being pressed
    def _do_polling(self):
        for rp in self._rowpins:
            GPIO.output(rp, GPIO.HIGH)
            for cp in self._columnpins:
                counter = 0
                while GPIO.input(cp) == GPIO.HIGH:
                    time.sleep(0.001)
                    counter += 1
                if counter >= 20:
                    return rp, cp
            # only one row pin should be high at a time
            GPIO.output(rp, GPIO.LOW)
        return None

    # initiates repeated calls to do_polling until a key press is detected
    # returns the button pressed as a string
    def wait_for_next_signal(self):
        signal = None
        while signal is None:
            time.sleep(0.1)
            signal = self._get_input_if_any()
        return signal
