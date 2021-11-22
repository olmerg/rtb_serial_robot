# -*- coding: utf-8 -*-
"""
This is the example to execute the planar3DOF robot

@author olmerg

"""
#import sys  
#sys.path.insert(0, 'planar_3d')

from Planar3DOF import Planar3DOF

import roboticstoolbox as rtb
import numpy as np
from math import pi

robot=Planar3DOF()
print(robot)
print(robot.links)

T =robot.fkine(robot.qs)
print(T)

#robot.plot(robot.qs,backend='swift')
from roboticstoolbox.backends.swift import Swift
env = Swift()
env.launch(realTime=True)
env.add(robot)

env.step(1.0)

qt = rtb.tools.trajectory.jtraj(np.array([0, 0, 0]), np.array([pi/2, pi/2, pi/2]), 20)
    
for q in qt.q:
         print(q)
         robot.q=q
         env.step(0.1)
    # return to home


#robot.teach(backend='pyplot')

