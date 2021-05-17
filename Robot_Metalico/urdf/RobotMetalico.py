import numpy as np
from roboticstoolbox.robot.ERobot import ERobot
from math import pi


class RobotMetalico(ERobot):
    """
    Class that imports a RobotMetalico 
    """

    def __init__(self):

        args = super().urdf_to_ets_args(
            "lesson_urdf/urdf/Robot_Metalico.urdf")
        
        super().__init__(
            args[0],
            name=args[1])

        self.manufacturer = "Utadeo"
        # self.ee_link = self.ets[9]

        # zero angles, L shaped pose
        self.addconfiguration("qa", np.array([0, 0, 0, 0, 0]))

        # ready pose, arm up
        self.addconfiguration("qb", np.array([pi/6, pi/4, -pi/4, pi/2, 0]))

if __name__ == '__main__':   # pragma nocover

    Robot = RobotMetalico()
    print(Robot)