# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:13:18 2021

@author: JCSCORPION
"""
import time
import sys  
sys.path.append( 'planar_3dof')
sys.path.append( '../Swift_serial')
import numpy as np
import roboticstoolbox as rtb
from Planar3DOF import Planar3DOF
from Swift_serial import Swift_serial
from math import pi

from roboticstoolbox import DHRobot,RevoluteMDH,PrismaticMDH
import roboticstoolbox as rtb
import numpy as np
from math import pi
import matplotlib.pyplot as plt
from spatialmath import *


if __name__ == '__main__':   # pragma nocover

    env = Swift_serial('COM3',115200)
    
    
    #posicion inicial (aqui cambiar por el robot realizado)
    
    robot=Planar3DOF()
    print(robot)
    print(robot.links)
    print(robot.qr)
    
    #robot.plot(robot.qr,backend='swift',block=True)
    print(robot.qz)
    #robot.plot(robot.qz)
    #print(robot.to_dict)
    # the robot should start in home 
    env.launch()
    env.add(robot)
    
    
    qz = np.array([0, 0, 0, 0, 0])
    q0 = np.array([-pi/2, 0.76, 0.82, 0, 0])
    q1 = np.array([0, 0.76, 0.82, 0, 0])
    #q2 = np.array([0, 0.76, pi/2, -0.72, 0])#ojo
    q2 = np.array([0, 1.135398163, 1.195398163, -0.72, 0])#ojo
    #0.3753981634*2
    q3 = np.array([-pi, 0.76, 0.82, 0, pi/2])
    q4 = np.array([-pi, 0.76, pi/2, -0.72, pi/2])
    q5 = np.array([-pi, 0.76, 0.82, pi/2, pi/2])
    q6 = np.array([-pi/2, 0.76, 0.82, 0, pi/2])
    
  
    
    
    Trayec0 = rtb.tools.trajectory.jtraj(qz, q0 , 20)
    Trayec1 = rtb.tools.trajectory.jtraj(q0, q1 , 20)
    Trayec2 = rtb.tools.trajectory.jtraj(q1, q2 , 20)
    Trayec3 = rtb.tools.trajectory.jtraj(q2, q1 , 20)
    Trayec4 = rtb.tools.trajectory.jtraj(q1, q0 , 20)
    Trayec5 = rtb.tools.trajectory.jtraj(q0, q6 , 20)
    Trayec6 = rtb.tools.trajectory.jtraj(q6, q3 , 20)
    Trayec7 = rtb.tools.trajectory.jtraj(q3, q5 , 20)
    
   
    
    
    env.activar_gripper()
    time.sleep(0.1)
    env.step(1.0)
    
    for q in Trayec0.q:
          print(q)
          robot.q=q
          env.step(0.1)
    
    
    
    for q in Trayec1.q:
          print(q)
          robot.q=q
          env.step(0.1)
    
    
    
    for q in Trayec2.q:
          print(q)
          robot.q=q
          env.step(0.1)
    
    env.desactivar_gripper()
    env.step(1.0)
    
    
    for q in Trayec3.q:
          print(q)
          robot.q=q
          env.step(0.1)
          
    # env.desactivar_gripper()
    # env.step(1.0)
    
    for q in Trayec4.q:
          print(q)
          robot.q=q
          env.step(0.1)
    
    
    for q in Trayec5.q:
          print(q)
          robot.q=q
          env.step(0.1)
    
    
    for q in Trayec6.q:
          print(q)
          robot.q=q
          env.step(0.1)
    
    
    for q in Trayec7.q:
          print(q)
          robot.q=q
          env.step(0.1)
          
    env.activar_gripper()
    env.step(1.0)
    #env.hold()        
    env.reset()
    
