# -*- coding: utf-8 -*-
"""
This is the example to execute the planar3DOF robot

@author olmerg

"""
import sys  
sys.path.append( 'planar_3dof')
sys.path.append( '../Swift_serial')
import numpy as np
import roboticstoolbox as rtb
from Planar3DOF import Planar3DOF
from Swift_serial import Swift_serial
from math import pi

if __name__ == '__main__':   # pragma nocover

    env = Swift_serial('COM4',115200)
    
    
    #posicion inicial (aqui cambiar por el robot realizado)
    robot=Planar3DOF()
    print(robot)
    print(robot.to_dict)
    # the robot should start in home 
    env.launch()
    env.add(robot)

    qt = rtb.tools.trajectory.jtraj(np.array([0, 0, 0]), np.array([pi/2, -pi/3, pi/2]), 20)
    
    for q in qt.y:
         print(q)
         robot.q=q
         env.step(0.1)
    # return to home
    env.reset()
    #qt.plot(block=True)


