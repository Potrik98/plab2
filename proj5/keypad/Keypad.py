import RPi.GPIO as GPIO
import time


class Keypad():

    # rowpins: contains all the pins connected to the board, corresponding to each row
    # columnpins: same, but with columns
    # dict:
    #   key (tuple(int, int)):  (rowpin, columnpin)
    #   value (string):         value of the button on keypad
    def __init__(self, rowpins, columnpins):
        self.rowpins = rowpins
        self.columnpins = columnpins
        self.dict = {}
        for i in range(len(rowpins)):
            for j in range(len(rowpins)):
                if i == 3:
                    if j == 0:
                        self.dict[(rowpins[i], columnpins[j])] = "*"
                    elif j == 1:
                        self.dict[(rowpins[i], columnpins[j])] = "0"
                    else:
                        self.dict[(rowpins[i], columnpins[j])] = "#"
                self.dict[(rowpins[i], columnpins[j])] = str(1+3*i+j)

    # initializes the row and column pins
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for rp in self.rowpins:
            GPIO.setup(rp, GPIO.OUT)
        for cp in self.columnpins:
            GPIO.setup(cp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # checks if any button is pressed
    # returns the location (row-pin, column-pin) as the one being pressed
    def do_polling(self):
        for rp in self.rowpins:
            GPIO.output(rp, GPIO.HIGH)
            for cp in self.columnpins:
                counter = 0
                while GPIO.input(cp) == GPIO.HIGH:
                    time.sleep(0.01)
                    counter += 1
                if counter >= 20:
                    return rp, cp
            GPIO.output(rp, GPIO.LOW)  # only one row pin should be high at a time
        return None

    # initiates repeated calls to do_polling until a key press is detected
    # returns the button pressed as a string
    def get_next_signal(self):
        button_pressed = None
        while button_pressed is None:
            button_pressed = self.do_polling
        return self.dict[button_pressed]
