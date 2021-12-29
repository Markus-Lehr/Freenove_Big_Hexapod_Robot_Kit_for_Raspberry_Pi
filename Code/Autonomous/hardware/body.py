import leg


class RobotBody:
    legs: [leg.Leg]

    def __init__(self):
        self.legs = [
            leg.LEG1,
            leg.LEG2,
            leg.LEG3,
            leg.LEG4,
            leg.LEG5,
            leg.LEG6
        ]
