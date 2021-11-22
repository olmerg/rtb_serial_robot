import numpy as np
from roboticstoolbox.robot.ERobot import ERobot
from math import pi
import os

class Planar3DOF(ERobot):
    """
    Class that imports a planar3DOF Robot
    """

    def __init__(self):

        args = super().URDF_read(
            "lesson_urdf/urdf/planar_3dof.urdf",tld=Planar3DOF.load_my_path())
        
        super().__init__(
            args[0],
            name=args[1])

        self.manufacturer = "Utadeo"
        # self.ee_link = self.ets[9]

        # zero angles, L shaped pose
        self.addconfiguration("qz", np.array([0, 0, 0, 0, 0]))

        # ready pose, arm up
        self.addconfiguration("qr", np.array([0, pi/2, -pi/2, 0, 0]))

        # straight and horizontal
        self.addconfiguration("qs", np.array([0, 0, -pi/2, 0, 0]))

        # nominal table top picking pose
        self.addconfiguration("qn", np.array([0, pi/4, pi, 0, 0]))
    @staticmethod
    def load_my_path():
            #print(__file__)
            os.chdir(os.path.dirname(__file__))
if __name__ == '__main__':   # pragma nocover

    robot = Planar3DOF()
    print(robot)