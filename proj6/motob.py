from motors import *
from Behavior import *

class Motob:
    def __init__(self):
        self.motors = Motors()

    def update(self, motor_recommendation):
        self.operationalize(motor_recommendation[0], motor_recommendation[1])

    # sets the right and left motors to left_speed and right_speed
    def operationalize(self, left_speed, right_speed):
        self.motors.set_left_speed(left_speed)
        self.motors.set_right_speed(right_speed)
