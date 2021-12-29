from .PCA9685 import PCA9685


def map_range(value: float, range_a: (float, float), range_b: (float, float)):
    return (range_b[1] - range_b[0]) * (value - range_a[0]) / (range_a[1] - range_a[0]) + range_b[0]


class ServoDriver:
    address: int
    channel: int
    _pwm: PCA9685

    def __init__(self, address, channel):
        self.address = address
        self.channel = channel
        self._pwm = PCA9685(address, debug=True)

    def set_pwm(self, off_timing, on_timing=0):
        self._pwm.setPWM(self.channel, int(on_timing), int(off_timing))

    def relax(self):
        self._pwm.setPWM(self.channel, 4096, 4096)


class Servo:
    angle: float = -1.0
    driver: ServoDriver

    def __init__(self, channel):
        if channel >= 32:
            print(f'Given channel {channel} must be less than 32')
            exit(1)

        if channel < 16:
            self.driver = ServoDriver(0x41, channel)
        else:
            self.driver = ServoDriver(0x40, channel - 16)

    def set_angle(self, angle: float):
        self.angle = angle
        pulse_length = map_range(angle, (0, 180), (500, 2500))  # angle to µs
        duty_cycle = map_range(pulse_length, (0, 20000), (0, 4095))  # µs to duty
        self.driver.set_pwm(duty_cycle)

    def relax(self):
        self.driver.relax()
