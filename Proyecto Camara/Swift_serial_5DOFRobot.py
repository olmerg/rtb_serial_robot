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

    #qt = rtb.tools.trajectory.jtraj(np.array([0, 0, 0,0,0]), np.array([pi/2, -pi/3, pi/2,pi/2,pi/2]), 80)

    p0=np.array([0, 0, 0, 0, 0])  
    p1=np.array([0, 0, 0, -pi/2, pi/2])
    p2=np.array([0, 0, -pi/2, 0, -pi/2])
    p3=np.array([-pi/2, 0, -pi/2, 0, 0])
    p4=np.array([0, -pi/2, pi/2, 0, 0])
    p5=np.array([pi/2, -pi/2, pi/2, -pi/2, 0])
    p6=np.array([0, 0, 0, -pi/2, 0])
    p7=np.array([0, 0, 0, 0, -pi/2])               

    q0 = rtb.tools.trajectory.jtraj(p0,p1,50)
    q1 = rtb.tools.trajectory.jtraj(p1,p2,50)
    q2 = rtb.tools.trajectory.jtraj(p2,p3,50)
    q3 = rtb.tools.trajectory.jtraj(p3,p4,100)
    q4 = rtb.tools.trajectory.jtraj(p4,p5,100)
    q5 = rtb.tools.trajectory.jtraj(p5,p6,100)    
    q6 = rtb.tools.trajectory.jtraj(p6,p7,100)

    #robot.plot(np.concatenate((q0.q,q1.q,q2.q,q3.q,q4.q,q5.q,q6.q)), block=False)

#for i in [0, 1, 2, 3, 4]:
    for q in q0.q:
         #print(q)
         robot.q=q
         env.step(0.01)
    for q in q1.q:
         #print(q)
         robot.q=q
         env.step(0.01)          
    for q in q2.q:
         #print(q)
         robot.q=q
         env.step(0.01) 
    for q in q3.q:
         #print(q)
         robot.q=q
         env.step(0.01) 
    for q in q4.q:
         #print(q)
         robot.q=q
         env.step(0.01) 
    for q in q5.q:
         #print(q)
          robot.q=q
          env.step(0.01)
    for q in q6.q:
         #print(q)
         robot.q=q
         env.step(0.01)
    # return to home
    env.reset()
    #env.close()
    #del env 
