from zumo_button import *
from camera import *
from ultrasonic import *
from reflectance_sensors import *
from sensob import *
from arbitrator import *
from motob import *


class BBcon:

    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motob = Motob()
        self.arbitrator = Arbitrator()

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)

    # add a newly active behavior to the active_behaviors list (if it exists in behaviors)
    def activate_behavior(self, active_behavior):
        if self.behaviors.__contains__(active_behavior):
            self.active_behaviors.append(active_behavior)

    # remove a newly deactived behavior from the active_behaviors list (if it exists in active_behaviors)
    def deactivate_behavior(self, deactive_behavior):
        if self.active_behaviors.__contains__(deactive_behavior):
            self.active_behaviors.remove(deactive_behavior)

    def run_one_timestep(self):
        # update all sensobs
        for sensob in self.sensobs:
            sensob.update()

        # update all behaviors
        for behavior in self.behaviors:
            behavior.update()
            if behavior.active_flag:
                self.activate_behavior(behavior)
            else:
                self.deactivate_behavior(behavior)

        recommended_behavior, halt_request = self.arbitrator.choose_action()

        # update motor object based on recommended_behavior
        self.motob.update(recommended_behavior)

        # wait
        time.sleep(1)

        # reset sensobs
        for sensob in self.sensobs:
            sensob.reset()

    def startup(self):
        # add sensor objects
        cam = Sensob(Camera())
        ultrasonic = Sensob(Ultrasonic())
        ir_sensor = Sensob(ReflectanceSensors())
        self.add_sensob(cam)
        self.add_sensob(ultrasonic)
        self.add_sensob(ir_sensor)

        button = ZumoButton()
        button.wait_for_press()
        while True:
            self.run_one_timestep()


if __name__ == "__main__":
    bbcon = BBcon()
    bbcon.startup()
