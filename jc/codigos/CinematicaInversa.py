# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 21:58:11 2021

@author: JCSCORPION
"""

from roboticstoolbox import DHRobot,RevoluteDH
import roboticstoolbox as rtb
import numpy as np
from math import pi


class RobotRPPR(DHRobot):
    def __init__(self):
        super().__init__(
            [
                RevoluteDH(d=100),
                RevoluteDH(d=100, alpha=pi/2),
                RevoluteDH(offset=pi/2,a=100),
                RevoluteDH(alpha=pi, a=100),
                RevoluteDH(a=100),

            ], name="Robot JC")
        self.addconfiguration("qz", np.array([0, 0, pi/2, 0, 0]))
        self.addconfiguration("qr", np.array([0, 0, 0, 0, 0]))

my_robot= RobotRPPR()
print(my_robot)

my_robot.q=my_robot.qz
my_robot.plot(my_robot.qr)

MatrizPosicionGripper = my_robot.fkine(my_robot.qz)
print(MatrizPosicionGripper)

my_robot.qz

MatrizMotores = my_robot.fkine_all(my_robot.qz)
print(MatrizPosicionGripper)

posicion_motores = np.array([0, 0, 0, 0, 0])
qt = rtb.jtraj(my_robot.qz, posicion_motores, 50)
my_robot.plot(qt.q, movie='ejemplo_robot_rppr.gif')

T = my_robot.fkine(my_robot.qr) #posicion del gripper
print(T)

sol=my_robot.ikine_LM(T)
print(sol)
print(my_robot.fkine(sol.q))
