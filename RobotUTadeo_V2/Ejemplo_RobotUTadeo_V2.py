# -*- coding: utf-8 -*-
"""
This is the example to execute the planar3DOF robot
@author olmerg
"""
import sys  
sys.path.insert(0, 'RobotUTadeo_V2')

from RobotUTadeo_V2 import RobotUTadeo_V2

import roboticstoolbox as rtb
import numpy as np
from math import pi

robot=RobotUTadeo_V2()
print(robot)
print(robot.links)

T =robot.fkine(robot.qs)
print(T)

#robot.plot(robot.qr,backend='swift')
from roboticstoolbox.backends.Swift import Swift
env = Swift()
env.launch()
env.add(robot)



qt = rtb.tools.trajectory.jtraj(np.array([0, 0, 0, 0 ,0]), np.array([pi/2, pi/2, -pi/2, pi/2, pi/2]), 20)
    
for q in qt.y:
         print(q)
         robot.q=q
         env.step(0.1)
    # return to home


#robot.teach(backend='pyplot')