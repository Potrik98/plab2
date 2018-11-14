from Behavior import Behavior
from motob import MotorOperation


class Arbitrator:
    def __init__(self, bbc):
        self.bbc = bbc

    # Chooses an action based on the weights and
    # returns the motor recommendation and halt flag
    def choose_action(self) -> (MotorOperation, bool):
        mx = -1
        action = None # Action is the selected behaviour
        for active_behavior in self.bbc.active_behaviors:
            if active_behavior.weight > mx:
                mx = active_behavior.weight
                action = active_behavior
        return action.motor_recommendation, action.halt_request
