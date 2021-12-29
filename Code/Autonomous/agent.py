import time

from .hardware import helper
from .hardware.body import RobotBody


class Agent:
    robot: RobotBody

    def __init__(self):
        helper.setup()
        self.robot = RobotBody()

    def point(self, angle):
        leg = self.robot.legs[0]
        leg.set_angles([angle, None, None])


if __name__ == '__main__':
    agent = Agent()
    angle = 0
    while angle <= 180:
        agent.point(angle)
        angle += 10
        time.sleep(1)
