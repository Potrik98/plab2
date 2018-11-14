class Sensob:
    def __init__(self, sensor):
        self.sensor = sensor

    # updates the sensor's value
    def update(self):
        self.sensor.update()

    # returns value that the sensor got
    def get_value(self):
        return self.sensor.get_value()

    # sets the sensor's value to None
    def reset(self):
        self.sensor.reset()
