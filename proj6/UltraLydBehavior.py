from Behavior import Behavior
from ultrasonic import *
from motob import MotorOperation


class UltraBehavior(Behavior):
    def __init__(self, bbcon):
        Behavior.__init__(self, bbcon)
        self.priority = 1.5

    def sense_and_act(self):
        distance = self.sensobs[1].sensor_get_value()
        self.halt_request = False
        self.match_degree = 1 - min(distance/10, 1)
        self.motor_recommendation = MotorOperation.BACKWARDS
