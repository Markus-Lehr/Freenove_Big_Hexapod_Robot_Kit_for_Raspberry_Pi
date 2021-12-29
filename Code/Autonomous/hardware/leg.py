from .servo import Servo


class Leg:
    servos: [Servo]

    def __init__(self, servo_channels: [int]):
        self.servos = [Servo(channel) for channel in servo_channels]

    def set_angles(self, angles: [float]):
        print(f'setting angles to: {angles}')
        if len(self.servos) != len(angles):
            print('the list of provided angles must be the same length as the list of servos')
            return
        for index, angle in enumerate(angles):
            if angle is not None:
                self.servos[index].set_angle(angle)

    def relax(self):
        for servo in self.servos:
            servo.relax()


LEG1 = Leg([15, 14, 13])
LEG2 = Leg([12, 11, 10])
LEG3 = Leg([9, 8, 31])
LEG4 = Leg([22, 23, 27])
LEG5 = Leg([19, 20, 21])
LEG6 = Leg([16, 17, 18])
