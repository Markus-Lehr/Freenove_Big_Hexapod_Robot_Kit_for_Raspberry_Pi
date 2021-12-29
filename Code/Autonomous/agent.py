import time

from hardware import helper
from hardware.body import RobotBody


class Agent:
    robot: RobotBody

    def __init__(self):
        helper.setup()
        self.robot = RobotBody()

    def point(self, angle):
        leg = self.robot.legs[0]
        leg.set_angles([angle, None, None])

    def relax(self):
        self.robot.relax()


if __name__ == '__main__':
    agent = Agent()
    agent.relax()
    angle = 0
    while angle <= 180:
        print(f'setting leg to angle {angle}')
        agent.point(angle)
        angle += 10
        time.sleep(5)
    agent.relax()
