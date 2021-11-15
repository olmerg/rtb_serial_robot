import numpy as np
from roboticstoolbox.robot.ERobot import ERobot
from math import pi


class RobotUTadeo_V2(ERobot):
    """
    Class that imports a RobotUTadeo_V2
    """

    def __init__(self):

        args = super().urdf_to_ets_args(
            "RobotUtadeo-V2.0/URDF/URDF-RobotUTadeo-V2.urdf")
        super().__init__(
            args[0],
            name=args[1])
            
        self.manufacturer = "UTadeo"
        # self.ee_link = self.ets[9]

        # zero angles, L shaped pose
        self.addconfiguration("qz", np.array([pi/2, pi/2, pi/2, pi/2, pi/2]))

        # ready pose, arm up
        self.addconfiguration("qr", np.array([0, 0, 0, 0, 0]))

if __name__ == '__main__':   # pragma nocover

    Robot = RobotUTadeo_V2()
    print(Robot)