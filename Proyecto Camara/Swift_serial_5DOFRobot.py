# -*- coding: utf-8 -*-
"""
This is the example to execute the Robot5DOF robot

@author olmerg

"""
import sys
#sys.path.append( 'Proyecto Camara') 
sys.path.append( 'Swift_serial')
import numpy as np
import roboticstoolbox as rtb
from Robot5DOF import Robot5DOF
from Swift_serial import Swift_serial
from math import pi

if __name__ == '__main__':   # pragma nocover

    env = Swift_serial('COM6',115200)
    
    
    #posicion inicial (aqui cambiar por el robot realizado)
    robot=Robot5DOF()
    print(robot)
    #print(robot.to_dict)
    # the robot should start in home 
    env.launch()
    env.add(robot)

    qt = rtb.tools.trajectory.jtraj(np.array([0, 0, 0]), np.array([pi/2, -pi/3, pi/2]), 20)
    
    for q in qt.q:
         print(q)
         robot.q=q
         env.step(0.1)
    # return to home
    env.reset()
    #qt.plot(block=True)