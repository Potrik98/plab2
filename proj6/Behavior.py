class Behavior:
    def __init__(self, bbcon):
        self.bbcon = bbcon
        self.sensobs = self.bbcon.sensobs
        self.motor_recommendation = 0
        self.active_flag = False            # indicates if the behavior is active or not
        self.halt_request = None
        self.priority = -1                  # indicates the importance of this behavior
        self.match_degree = 0               # float between 0 and 1
        self.weight = 0                     # basis to decide whether to use this behavior or not

    def consider_deactivation(self):
        #if not self.bbcon.status[self]:
        self.active_flag = True

    def consider_activation(self):
        #if self.bbcon.status[self]:
        self.active_flag = True

    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()
        if not self.active_flag:
            return
        self.sense_and_act()
        self.weight = self.match_degree * self.priority

    # Sets the motor recommendations
    def sense_and_act(self):
        raise NotImplementedError()
