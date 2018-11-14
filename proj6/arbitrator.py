class Arbitrator:
    def __init__(self, bbc):
        self.bbc = bbc

    def choose_action(self):
        mx = -1
        action = None
        for active_behavior in self.bbc.active_behaviors:
            if active_behavior.weight > mx:
                mx = active_behavior.weight
                action = active_behavior
        return action, action.halt_request

