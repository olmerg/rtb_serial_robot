  
# -*- coding: utf-8 -*-
"""
This is the example to execute the planar3DOF robot
@author olmerg
"""
import sys  
sys.path.insert(0, 'RobotUtadeo')

from RobotUtadeo import RobotUtadeo

import roboticstoolbox as rtb
import numpy as np
from math import pi

robot=RobotUtadeo()
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