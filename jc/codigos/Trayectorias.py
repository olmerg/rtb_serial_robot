# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:41:43 2021

@author: JCSCORPION
"""

from roboticstoolbox import DHRobot,RevoluteDH,PrismaticDH
import roboticstoolbox as rtb
import numpy as np
from math import pi
import matplotlib.pyplot as plt
from spatialmath import *
from roboticstoolbox.backends.swift import Swift

from Planar3DOF import Planar3DOF

robot=Planar3DOF()

print(robot) 
print(robot.links)
print(robot.qr)
print(robot.qz)


q0 = np.array([-pi/2, 0.76, 0.82, 0, 0])
q1 = np.array([0, 0.76, 0.82, 0, 0])
q2 = np.array([0, 0.76, pi/2, -0.72, 0])#ojo
q3 = np.array([-pi, 0.76, 0.82, 0, pi/2])
q4 = np.array([-pi, 0.76, pi/2, -0.72, pi/2])
q5 = np.array([-pi, 0.76, 0.82, pi/2, pi/2])
q6 = np.array([-pi/2, 0.76, 0.82, 0, pi/2])

Trayec1 = rtb.jtraj(q0, q1 , 150)
Trayec2 = rtb.jtraj(q1, q2 , 150)
Trayec3 = rtb.jtraj(q2, q1 , 150)
Trayec4 = rtb.jtraj(q1, q0 , 150)
Trayec5 = rtb.jtraj(q0, q6 , 150)
Trayec6 = rtb.jtraj(q6, q3 , 150)
Trayec7 = rtb.jtraj(q3, q5 , 150)


robot.plot( np.concatenate(( Trayec1.q, Trayec2.q, Trayec3.q, Trayec4.q, Trayec5.q, Trayec6.q, Trayec7.q)), block=False)

# Punto1=SE3(x=282,y=282,z=116)
# Punto2=SE3(x=282,y=282,z=350)
# #P3=SE3(x=282,y=282,z=116)
# #P4=SE3(x=282,y=282,z=116)

# trayegrafc1=rtb.ctraj(Punto1, Punto2, 150)

# trayegrafc1.plot()

# P1=SE3(x=2.82,y=2.82,z=1.16)
# P2=SE3(x=2.82,y=2.82,z=3.50)

# pp1 = robot.ikine_min(P1)
# pp1 = robot.ikine_min(P2)

# TrayC1=rtb.ctraj(P1, P2, 150)

# InvertrayecC1=robot.ikine_min(TrayC1)

# Trayec1 = rtb.jtraj(InvertrayecC1[0].q, InvertrayecC1[-1].q, 150)

# robot.plot(Trayec1.q,block=False)

# from roboticstoolbox.backends.swift import Swift

# backend = Swift()
# backend.launch()

# backend.add(robot)

# for x in Trayec1.q:
#     robot.q = x
#     backend.step()

#p1 = SE3(X=0, Y=0, Z=0)
 #punto1 = (282, 282, 116)
 #punto2 = (  282 282 350)
 #punto3=SE3( x=370, y=255, z=116)
 #punto4=SE3( x=370, y=255, z=350)

#trayegrafc1=rtb.ctraj(punto1, punto2, 150)
# trayegrafc2=rtb.ctraj(punto3, punto2, 150)
# trayegrafc3=rtb.ctraj(punto2, punto1, 150)

# trayegrafc1.plot()
# trayegrafc2.plot()
# trayegrafc3.plot()

# P1=SE3(x=3.0,y=2.5,z=2.0)
# P2=SE3(x=3.0,y=2.5,z=0.8)
# P3=SE3(x=3.7,y=2.5,z=0.8)
# P4=SE3(x=3.7,y=2.5,z=6.0)

# pp1 = robot.ikine_min(P1)
# pp2 = robot.ikine_min(P2)
# pp3 = robot.ikine_min(P3)
# pp4 = robot.ikine_min(P4)

# TrayC1=rtb.ctraj(P4, P3, 150)
# TrayC2=rtb.ctraj(P3, P2, 150)
# TrayC3=rtb.ctraj(P2, P1, 150)

# InvertrayecC1=robot.ikine_min(TrayC1)
# InvertrayecC2=robot.ikine_min(TrayC2)
# InvertrayecC3=robot.ikine_min(TrayC3)

# Trayec1 = rtb.jtraj(InvertrayecC1[0].q, InvertrayecC1[-1].q, 150)
# Trayec2 = rtb.jtraj(InvertrayecC2[0].q, InvertrayecC2[-1].q, 150)
# Trayec3 = rtb.jtraj(InvertrayecC3[0].q, InvertrayecC3[-1].q, 150)

# robot.plot(Trayec1.q,block=False)
# robot.plot(Trayec2.q,block=False)
# robot.plot(Trayec3.q,block=False)

# traj = rtb.jtraj(pp1.q, pp2.q, np.arange(0,10,0.1), qd0=np.array([pi/4, 0.5, pi/4, 0.5, pi/4, 0.5]),qd1=np.array([pi/4, 0.5, pi/4, 0.5, pi/4, 0.5]))
# traj.plot()

# #velocidad del gripper en cada punto
# vg1 = robot.jacob0(pp1.q)
# vg2 = robot.jacob0(pp2.q)
# vg3 = robot.jacob0(pp3.q)
# vg4 = robot.jacob0(pp4.q)

# #velocidad de los motores en cada punto
# vm1=np.linalg.pinv(robot.jacob0(pp1.q))
# vm2=np.linalg.pinv(robot.jacob0(pp2.q))
# vm3=np.linalg.pinv(robot.jacob0(pp3.q))
# vm4=np.linalg.pinv(robot.jacob0(pp4.q))

# #robot.q = pp3.q
# from roboticstoolbox.backends.swift import Swift

# backend = Swift()
# backend.launch()

# backend.add(robot)

# #gif = [Trayec1.q, Trayec1.q, Trayec1.q, Trayec1.q]

# for x in Trayec1.q:
#     robot.q = x
#     backend.step()
# for x in Trayec2.q:
#     robot.q = x
#     backend.step()
# for x in Trayec3.q:
#     robot.q = x
#     backend.step()



