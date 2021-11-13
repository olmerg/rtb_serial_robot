import numpy as np
from roboticstoolbox.robot.ERobot import ERobot
from math import pi
import os

class Robot5DOF(ERobot):
    """
    Class that imports a 5DOF Robot
    """

    def __init__(self):

        args = super().URDF_read(
            "urdf/planar_3dof.urdf",tld=Robot5DOF.load_my_path())
        
        super().__init__(
            args[0],
            name=args[1])

        self.manufacturer = "Utadeo"
        # self.ee_link = self.ets[9]

        # zero angles, L shaped pose
        self.addconfiguration("qz", np.array([0, 0, 0, 0, 0]))

        # ready pose, arm up
        self.addconfiguration("qr", np.array([0, 0, 0, 0, 0]))

        # straight and horizontal
        self.addconfiguration("qs", np.array([0, 0, 0, 0, 0]))

        # nominal table top picking pose
        self.addconfiguration("qn", np.array([0, 0, 0, 0, 0]))
    @staticmethod
    def load_my_path():
            #print(__file__)
            os.chdir(os.path.dirname(__file__))
if __name__ == '__main__':   # pragma nocover

    robot = Robot5DOF()
    print(robot)