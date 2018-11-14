from Behavior import Behavior
from motob import MotorOperation
from imager2 import *
from camera import *


class CameraBehavior(Behavior):
    def __init__(self, bbcon):
        Behavior.__init__(self, bbcon)
        self.priority = 2

    def sense_and_act(self):
        image = self.sensobs[0].get_value()
        width, height = image.size
        imager = Imager(width=width, height=height)
        image_wta = imager.map_color_wta(image)
        rgb_im = image_wta

        redamount = 0
        pixelamount = width * height;
        for x in range(width):
            for y in range(height):
                if rgb_im.get_pixel(x, y) == Imager._pixel_colors_['red']:
                    redamount += 1

        self.halt_request = False
        self.match_degree = redamount/pixelamount
        self.motor_recommendation = MotorOperation.STOP
