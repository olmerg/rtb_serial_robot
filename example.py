# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 06:12:26 2021
- Add serial conection to your user in linux (if it can not find serial port): 
     sudo usermod -a -G dialout name_user
- please install pySerial
pip install pyserial

@author: olmer Garcia
"""
import numpy as np
import roboticstoolbox as rtb
from Swift_serial import Swift_serial
from math import pi


if __name__ == '__main__':   # pragma nocover

    robot = rtb.models.UR3()
    # print(robot)
    # robot.plot(,block=True)

    env = Swift_serial('/dev/ttyUSB0', 115200)
    env.launch(realtime=False)

    # posicion inicial (aqui cambiar por el robot realizado)

    # the robot should start in home

    env.add(robot)
    # animar generando una trayectoria
    n = 20  # numero de pasos a realizar
    Ts = 0.1  # cada cuando hacerlos(Tiempo de muestreo)
    tiempo = np.linspace(0, n*Ts, n)  # vector de tiempo
    qt = rtb.tools.trajectory.jtraj(np.array(
        [pi/2, -pi/2, 0, -pi/2, 0, 0]), np.array([pi/2, 0, 0, pi/2, 0, 0]), tiempo)
    for q in qt.q:
        print(q)
        robot.q = q
        env.step(0.1)
    # return to home
    env.reset()
    qt.plot(block=True)
