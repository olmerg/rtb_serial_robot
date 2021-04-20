# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 06:12:26 2021

please install pySerial
pip install pyserial

@author: olmer
"""
import numpy as np
import roboticstoolbox as rtb
from Swift_serial import Swift_serial
from math import pi


if __name__ == '__main__':   # pragma nocover

    env = Swift_serial('COM4',115200)
    env.launch()
    
    #posicion inicial (aqui cambiar por el robot realizado)
    robot = rtb.models.UR3()
    # the robot should start in home 
    
    env.add(robot)
    
    
    # animar generando una trayectoria
    qt = rtb.tools.trajectory.jtraj(np.array([0, 0, 0, 0,0, 0]), np.array([pi/2,0, pi/2, pi/2,pi/2, 0]), 20)
    
    for q in qt.y:
         print(q)
         robot.q=q
         env.step(0.1)
    # return to home
    env.reset()
    qt.plot(block=True)
    