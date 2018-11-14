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
            print("behaviour weight:", active_behavior.__class__, active_behavior.weight)
            if active_behavior.weight > mx:
                mx = active_behavior.weight
                action = active_behavior
        print("selecting action", action.__class__)
        return action.motor_recommendation, action.halt_request
