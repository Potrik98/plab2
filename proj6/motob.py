from motors import *
from behavior import *

class Motob:
    def __init__(self):
        self.motors = Motors()
        self.value = None

    def update(self, recommended_behavior):
        self.operationalize(recommended_behavior.motor_recommendations)

    # settings should be a list consisting of max 3 elements:
    #   action (string/character), speed (float [-1, 1]), duration (time in seconds)
    def operationalize(self, settings):
        if settings[0] == 'L':
            self.motors.left(settings[1], settings[2])
        elif settings[0] == 'R':
            self.motors.right(settings[1], settings[2])
        elif settings[0] == 'D':
            self.dance()

    def dance(self):
        self.motors = Motors()
        self.motors.forward(.2, 3)
        self.motors.backward(.2, 3)
        self.motors.right(.5, 3)
        self.motors.left(.5, 3)
        self.motors.backward(.3, 2.5)
        self.motors.set_value([.5, .1], 10)
        self.motors.set_value([-.5, -.1], 10)
