# -*- coding: utf-8 -*-
"""
This is the example to execute the RobotUTadeo_V2
@author olmerg
"""
import sys  
sys.path.append('RobotUTadeo_V2')

# ../ se devuelve hasta escontrar la carpeta Swift_serial
sys.path.append( 'Swift_serial')
import numpy as np
import roboticstoolbox as rtb
from RobotUTadeo_V2 import RobotUTadeo_V2
from Swift_serial import Swift_serial
from math import pi

if __name__ == '__main__':   # pragma nocover

    env = Swift_serial('COM6',115200)
    
    #posicion inicial (aqui cambiar por el robot realizado)
    robot=RobotUTadeo_V2()
    print(robot)
    print(robot.to_dict)
    # the robot should start in home 
    env.launch()
    env.add(robot)
    
    p0=np.array([0, 0, 0, 0, 0])  
    p1=np.array([pi/2, 0, 0, 0, 0])
    p2=np.array([pi/2, pi/2, pi/2,-pi/2, 0])
    p3=np.array([pi/2, pi/2, -(5*pi/36), pi/12, 0])
    p4=np.array([pi/2, 0, pi/4, (2*pi/9), 0])
    p5=np.array([-pi/2, 0, pi/4, (2*pi/9), 0])
    p6=np.array([-pi/2, pi/2, -pi/4, (2*pi/9), 0])
    p7=np.array([-pi/2, pi/2, -pi/4, (2*pi/9), pi/2])               

    q0 = rtb.tools.trajectory.jtraj(p0,p1,90)
    q1 = rtb.tools.trajectory.jtraj(p1,p2,90)
    q2 = rtb.tools.trajectory.jtraj(p2,p3,90)
    q3 = rtb.tools.trajectory.jtraj(p3,p4,90)
    q4 = rtb.tools.trajectory.jtraj(p4,p5,90)
    q5 = rtb.tools.trajectory.jtraj(p5,p6,90)    
    q6 = rtb.tools.trajectory.jtraj(p6,p7,90)        
    
    #env.reset()
for i in [0, 1, 2]:
    for q in q0.y:
         #print(q)
         robot.q=q
         env.step(0.01)
    for q in q1.y:
         #print(q)
         robot.q=q
         env.step(0.01)          
    for q in q2.y:
         #print(q)
         robot.q=q
         env.step(0.01) 
    for q in q3.y:
         #print(q)
         robot.q=q
         env.step(0.01) 
    for q in q4.y:
         #print(q)
         robot.q=q
         env.step(0.01) 
    for q in q5.y:
         #print(q)
         robot.q=q
         env.step(0.01)
    for q in q6.y:
         #print(q)
         robot.q=q
         env.step(0.01)
    # return to home
    env.reset()
    #env.close()
    #del env 
    #del robot
    #qt.plot(block=True) 
