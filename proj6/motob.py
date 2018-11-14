from motors import Motors

class Motob:
    def __init__(self):
        self.motors = Motors()

    def update(self, motor_recommendation):
        print(motor_recommendation)
        self.operationalize(motor_recommendation[0], motor_recommendation[1])

    # sets the right and left motors to left_speed and right_speed
    def operationalize(self, left_speed, right_speed):
        self.motors.forward(0.5)

