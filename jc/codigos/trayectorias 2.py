# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:11:52 2021

@author: JCSCORPION
"""

from roboticstoolbox import DHRobot,RevoluteDH,PrismaticDH
import roboticstoolbox as rtb
import numpy as np
from math import pi
import matplotlib.pyplot as plt
from spatialmath import *
#!pip install pyserial

from Planar3DOF import Planar3DOF
robot=Planar3DOF()
print(robot)
print(robot.links)

print(robot.qs)
robot.plot(robot.qs)