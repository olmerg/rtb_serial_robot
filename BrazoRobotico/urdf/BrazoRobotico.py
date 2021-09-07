import numpy as np
from roboticstoolbox.robot.ERobot import ERobot
from math import pi


class BrazoRobotico(ERobot):
    """
    Class that imports a BrazoRobotico
    """

    def __init__(self):

        args = super().urdf_to_ets_args(
            "lesson_urdf/urdf/BrazoRobotico.urdf")
        
        super().__init__(
            args[0],
            name=args[1])

        self.manufacturer = "Brazo"
        # self.ee_link = self.ets[9]

        # zero angles, L shaped pose
        self.addconfiguration("qz", np.array([0, 0, 0, 0, 0]))

        # ready pose, arm up
        self.addconfiguration("qr", np.array([0, pi/2, pi/2, pi/2, pi/2]))

if __name__ == '__main__':   # pragma nocover

    Robot = BrazoRobotico()
    print(Robot)