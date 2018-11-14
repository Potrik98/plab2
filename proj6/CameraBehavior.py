from Behavior import Behavior
from motob import MotorOperation
from camera import *
import math


class CameraBehavior(Behavior):
    def __init__(self, bbcon):
        Behavior.__init__(self, bbcon)
        self.priority = 2

    def sense_and_act(self):
        image = self.sensobs[0].get_value()
        image.thumbnail((1, 1))
        c = image.getpixel((0, 0))
        print("Average pixel value:", c)
        r = c[0]
        g = c[1]
        b = c[2]
        l = max(math.sqrt(r * r + g * g + b * b), 0.01)
        r /= l
        g /= l
        b /= l
        redness = min(max(2 * r - (b + g), 0), 1)
        print("redness: ", redness)

        self.halt_request = False
        self.match_degree = redness
        self.motor_recommendation = MotorOperation.TURN_RIGHT

    def consider_deactivation(self):
        distance = self.sensobs[1].get_value()
        distance_degree = 1 / max(distance - 10, 1)
        if distance_degree <= 0.5:
            self.active_flag = False

    def consider_activation(self):
        distance = self.sensobs[1].get_value()
        distance_degree = 1 / max(distance - 10, 1)
        if distance_degree > 0.5:
            self.active_flag = True
