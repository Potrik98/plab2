from Behavior import Behavior
from ultrasonic import *


class UltraBehavior(Behavior):
    def __init__(self, bbcon):
        Behavior.__init__(self, bbcon)

    def sense_and_act(self):
        distance = self.sensobs[1].sensor_get_value()
        half_request = False
        match_degree = min(distance, 1)
        motor_recommendation = [-1, -1]
        return half_request, match_degree, motor_recommendation
