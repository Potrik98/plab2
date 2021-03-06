from Behavior import Behavior
from motob import MotorOperation

class IRBehavior(Behavior):
    def __init__(self, bbcon):
        Behavior.__init__(self, bbcon)
        self.priority = 2

    def sense_and_act(self):
        value_list = self.sensobs[2].get_value()
        self.halt_request = False
        i = 0
        for value in value_list:
            i += value
        self.match_degree = max(((6 - i)/6 - 0.5) * 2,0)
        self.motor_recommendation = MotorOperation.TURN_LEFT
