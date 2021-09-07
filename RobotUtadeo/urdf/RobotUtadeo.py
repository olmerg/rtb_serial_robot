import numpy as np
from roboticstoolbox.robot.ERobot import ERobot
from math import pi


class RobotUtadeo(ERobot):
    """
    Class that imports a RobotUtadeo 
    """

    def __init__(self):

        args = super().urdf_to_ets_args(
            "lesson_urdf/urdf/Robot_Utadeo.urdf")
        
        super().__init__(
            args[0],
            name=args[1])

        self.manufacturer = "Utadeo"
        # self.ee_link = self.ets[9]

        # zero angles, L shaped pose
        self.addconfiguration("qz", np.array([pi/2, pi/2, pi/2, pi/2, pi/2]))

        # ready pose, arm up
        self.addconfiguration("qr", np.array([0, 0, 0, 0, 0]))

if __name__ == '__main__':   # pragma nocover

    Robot = RobotUtadeo()
    print(Robot)