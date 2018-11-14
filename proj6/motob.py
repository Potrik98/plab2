from motors import Motors
from enum import Enum


class MotorOperation(Enum):
    STOP = 5
    FORWARDS = 1
    BACKWARDS = 2
    TURN_LEFT = 3
    TURN_RIGHT = 4


class Motob:
    def __init__(self):
        self.motors = Motors()

    def update(self, motor_recommendation: MotorOperation):
        print(motor_recommendation)
        if motor_recommendation == MotorOperation.FORWARDS:
            self.motors.forward()
        elif motor_recommendation == MotorOperation.BACKWARDS:
            self.motors.backward()
        elif motor_recommendation == MotorOperation.TURN_LEFT:
            self.motors.left(1, 2.5)
        elif motor_recommendation == MotorOperation.TURN_RIGHT:
            self.motors.right(1, 2.5)
        else:
            self.motors.forward(0)
