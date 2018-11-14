from Behavior import Behavior
from imager2 import *
from camera import *


class CameraBehavior(Behavior):
    def __init__(self, bbcon):
        Behavior.__init__(self, bbcon)

    def sense_and_act(self):
        image = self.sensobs[0].sensor_get_value()
        imagewta = Imager.map_color_wta(image)
        width, height = imagewta.size
        rgb_im = imagewta.convert('RGB')

        redamount = 0
        pixelamount = width * height;
        for x in range(width):
            for y in range(height):
                if rgb_im.getpixel((x, y)) == Imager._pixel_colors_['red']:
                    redamount += 1

        half_request = False
        match_degree = redamount/pixelamount
        motor_recommendation = (-1, -1)
        return half_request, match_degree, motor_recommendation
