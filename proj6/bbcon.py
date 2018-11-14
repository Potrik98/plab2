from zumo_button import ZumoButton
from camera import Camera
from ultrasonic import Ultrasonic
from reflectance_sensors import ReflectanceSensors
from sensob import Sensob
from arbitrator import Arbitrator
from motob import Motob
from StandardBehavior import StandardBehavior
from CameraBehavior import CameraBehavior
from UltraLydBehavior import UltraBehavior
from IRBehavior import IRBehavior
import time


class BBcon:
    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motob = Motob()
        self.arbitrator = Arbitrator(self)
        self._running = False

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)

    # add a newly active behavior to the active_behaviors list
    # (if it exists in behaviors)
    def activate_behavior(self, active_behavior):
        if self.behaviors.__contains__(active_behavior) and \
                active_behavior not in self.active_behaviors:
            self.active_behaviors.append(active_behavior)

    # remove a newly deactived behavior from the active_behaviors list
    # (if it exists in active_behaviors)
    def deactivate_behavior(self, deactive_behavior):
        if self.active_behaviors.__contains__(deactive_behavior):
            self.active_behaviors.remove(deactive_behavior)

    def run_one_timestep(self):
        # update all sensobs
        for i in range(len(sensob)):
            if !(i == 0 && behavior[1].active_flag == false):
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

        # reset sensobs
        for sensob in self.sensobs:
            sensob.reset()

        # Stop running if a halt is requested
        if halt_request:
            self._running = False

    def startup(self):
        # add sensor objects
        cam = Sensob(Camera())
        ultrasonic = Sensob(Ultrasonic())
        ir_sensor = Sensob(ReflectanceSensors())
        self.add_sensob(cam)
        self.add_sensob(ultrasonic)
        self.add_sensob(ir_sensor)
        
        # add behaviors
        sb = StandardBehavior(self)
        self.add_behavior(sb)
        self.activate_behavior(sb)
        cb = CameraBehavior(self)
        self.add_behavior(cb)
        self.activate_behavior(cb)
        ub = UltraBehavior(self)
        self.add_behavior(ub)
        self.activate_behavior(ub)
        ir = IRBehavior(self)
        self.add_behavior(ir)
        self.activate_behavior(ir)
        
        button = ZumoButton()
        button.wait_for_press()
        self._running = True
        while self._running:
            self.run_one_timestep()
            # wait
            time.sleep(1)


if __name__ == "__main__":
    bbcon = BBcon()
    bbcon.startup()
