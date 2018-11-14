from Behavior import Behavior


class StandardBehavior(Behavior):
    def __init__(self, bbcon):
        Behavior.__init__(self, bbcon)
        self.priority = 1

    def sense_and_act(self):
        self.halt_request = False
        self.match_degree = 1
        self.motor_recommendation = [1, 1]
