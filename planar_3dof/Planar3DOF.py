import numpy as np
from roboticstoolbox.robot.ERobot import ERobot
from math import pi


class Planar3DOF(ERobot):
    """
    Class that imports a planar3DOF Robot
    """

    def __init__(self):

        args = super().urdf_to_ets_args(
            "lesson_urdf/urdf/planar_3dof.urdf")
        
        super().__init__(
            args[0],
            name=args[1])

        self.manufacturer = "Utadeo"
        # self.ee_link = self.ets[9]

        # zero angles, L shaped pose
        self.addconfiguration("qz", np.array([0, 0, 0]))

        # ready pose, arm up
        self.addconfiguration("qr", np.array([0, pi/2, -pi/2]))

        # straight and horizontal
        self.addconfiguration("qs", np.array([0, 0, -pi/2]))

        # nominal table top picking pose
        self.addconfiguration("qn", np.array([0, pi/4, pi]))
if __name__ == '__main__':   # pragma nocover

    robot = Planar3DOF()
    print(robot)