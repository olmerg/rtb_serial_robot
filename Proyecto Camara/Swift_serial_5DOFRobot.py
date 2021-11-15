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

    env = Swift_serial('COM4',115200)
    
    
    #posicion inicial (aqui cambiar por el robot realizado)
    robot=Robot5DOF()
    print(robot)
    # print(robot.to_dict)
    # the robot should start in home 
    env.launch()
    env.add(robot)

    qt = rtb.tools.trajectory.jtraj(np.array([0, 0, 0,0,0]), np.array([pi/2, -pi/3, pi/2,pi/2,pi/2]), 20)

    p0=np.array([0, 0, 0, 0, 0])  
    p1=np.array([pi/2, 0, 0, 0, 0])
    p2=np.array([pi/2, pi/2, pi/2,-pi/2, 0])
    p3=np.array([pi/2, pi/2, -(5*pi/36), pi/12, 0])
    p4=np.array([pi/2, 0, pi/4, (2*pi/9), 0])
    p5=np.array([-pi/2, 0, pi/4, (2*pi/9), 0])
    p6=np.array([-pi/2, pi/2, -pi/4, (2*pi/9), 0])
    p7=np.array([-pi/2, pi/2, -pi/4, (2*pi/9), pi/2])               

    q0 = rtb.tools.trajectory.jtraj(p0,p1,80)
    q1 = rtb.tools.trajectory.jtraj(p1,p2,180)
    q2 = rtb.tools.trajectory.jtraj(p2,p3,195)
    q3 = rtb.tools.trajectory.jtraj(p3,p4,195)
    q4 = rtb.tools.trajectory.jtraj(p4,p5,190)
    q5 = rtb.tools.trajectory.jtraj(p5,p6,215)    
    q6 = rtb.tools.trajectory.jtraj(p6,p7,225)

    for q in qt.q:
         print(q)
         robot.q=q
         env.step(0.1)
    # return to home
    env.reset()
    #qt.plot(block=True)
