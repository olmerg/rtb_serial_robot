# Robot Metálico
Hecho por:
Luis Angel Silva Rua, 
Diego Alberto Sanchez Lesmes, 
Juan david Cáceres es camilla, 
Nelson Manuel guerrero.

# Pruebas del segundo corte
#----------------------------------------#
#              LIBRERIAS                          # 
#----------------------------------------#
from roboticstoolbox import DHRobot
import time
import roboticstoolbox as rtb
import numpy as np
from math import pi
import matplotlib.pyplot as plt
from spatialmath import * 
#----------------------------------------#
#----------------------------------------#
from RobotMetalico import RobotMetalico
My_Robot=RobotMetalico()
#----------------------------------------#
#------------------------------------------------------#
#                     POSICIÓN HOME                             # 
#------------------------------------------------------#
My_Robot.plot(My_Robot.qa,backend='swift',block=False)
#------------------------------------------------------#

#----------------------------------------#
#             COORDENADAS x,y,z          # 
#----------------------------------------#
T_1=SE3(  x=85, y=255, z=85 )
T_2=SE3(  x=85, y=255, z=435)
T_3=SE3( x=370, y=255, z=85 )
T_4=SE3( x=370, y=255, z=435 )
#----------------------------------------#

#----------------------------------------#
#             MÉTODO CTRAJ                  #
#  para calcular trayectoria cartesiana  # 
#----------------------------------------#
L_1=rtb.ctraj(T_1, T_2, 133)
L_2=rtb.ctraj(T_2, T_3, 133)
L_3=rtb.ctraj(T_3, T_4, 133)
#----------------------------------------#

#----------------------------------------#
#             VISUALIZACIÓN                  #
#                LETRA N                            # 
#----------------------------------------#
L_1.plot()
L_2.plot()
L_3.plot()
#----------------------------------------#
#----------------------------------------#
#             COORDENADAS x,y,z          # 
#----------------------------------------#
T1=SE3(  x=85.0, y=255.0, z=85.0  )
T2=SE3(  x=85.0, y=255.0, z=435.0 )
T3=SE3( x=370.0, y=255.0, z=85.0  )
T4=SE3( x=370.0, y=255.0, z=435.0 )
#----------------------------------------#


#----------------------------------------#
#             MÉTODO ctraj               #
#  para calcular trayectoria cartesiana  # 
#----------------------------------------#
L1=rtb.ctraj(T1, T2, 75)
L2=rtb.ctraj(T2, T3, 75)
L3=rtb.ctraj(T3, T4, 75)
#----------------------------------------#


#-----------------------------------#
#         CINEMÁTICA INVERSA        #
#-----------------------------------#
Cinem_inver1=My_Robot.ikine_min(L1)
Cinem_inver2=My_Robot.ikine_min(L2)
Cinem_inver3=My_Robot.ikine_min(L3)
#-----------------------------------#


#-------------------------------------------------------------#
#                        MÉTODO jtraj                         #
#            para calcular trayectoria articular              # 
#-------------------------------------------------------------#
Mov1 = rtb.jtraj(Cinem_inver1[0].q, Cinem_inver1[-1].q, 135)
Mov2 = rtb.jtraj(Cinem_inver2[0].q, Cinem_inver2[-1].q, 135)
Mov3 = rtb.jtraj(Cinem_inver3[0].q, Cinem_inver3[-1].q, 135)
#-------------------------------------------------------------#
# Simulación del robot en 'swift'
#--------------------------------
My_Robot.plot(Mov1.y,block=False)
time.sleep(1.3)
#--------------------------------
My_Robot.plot(Mov2.y,block=False)
time.sleep(1.3)
#--------------------------------
My_Robot.plot(Mov3.y,block=False)
#--------------------------------

 # Grados de libertad y como usar el planeamiento de trayectorias.
 ![](data:image/jpeg;base64,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)

- Cintura: Rango de movimiento de 0° hasta 180°, Peso max de carga. 8.5 kgf·cm (4.8 V ), 10 kgf*cm (6 V)
- Hombro: Rango de movimiento de 0° hasta 180°, Peso max de carga. 8.5 kgf·cm (4.8 V ), 10 kgf*cm (6 V)
- Codo:  Rango de movimiento de 0° hasta 180°, Peso max de carga. 8.5 kgf·cm (4.8 V ), 10 kgf*cm (6 V)
- Muñeca:  Rango de movimiento de 0° hasta 180°, Peso max de carga. 8.5 kgf·cm (4.8 V ), 10 kgf*cm (6 V)
- Mano:  Rango de movimiento de 0° hasta 180°, Peso max de carga. 1.8 kgf·cm
Sabiendo ya los rangos que alcanza cada una de las articulaciones, el siguiente paso a seguir es usar el planeamiento de trayectorias.
el método que vamos a usar es** jtraj** al igual que en las pruebas del corte anterior.

Empezamos definiendo la posición Home, y luego establece diferentes ágnulos hasta obtener la trayectoria deseada.
> Para establecer los ángulos que queremos en cada grado de libertad debemos tener en cuenta los rangos en los que se pueden mover.  

como se aprecia en el siguiente código establecimos 5 trayectorias en las cuales le definimos el punto de inicio y el punto de partida
#--------------------------------------------------------------------------------------------------------
    Tray1 = rtb.tools.trajectory.jtraj([0, 0, 0, 0, 0],[0, (2*pi/9), (2*pi/9), (-pi/3), 0],120)
    Tray2 = rtb.tools.trajectory.jtraj([0, (2*pi/9), (2*pi/9), (-pi/3), 0],[pi/2, (2*pi/9), (2*pi/9), (pi/3), 0],120)  
    Tray3 = rtb.tools.trajectory.jtraj([pi/2, (2*pi/9), (2*pi/9), (pi/3), 0],[0, 0, 0, 0, 0],120) 
    Tray4 = rtb.tools.trajectory.jtraj([0, 0, 0, 0, 0],[0, (2*pi/9), (2*pi/9), (-pi/3), 0],120)  
    Tray5 = rtb.tools.trajectory.jtraj([0, (2*pi/9), (2*pi/9), (-pi/3), 0],[-pi/2, (2*pi/9), (2*pi/9), (pi/3), 0],120) 
#--------------------------------------------------------------------------------------------------------

A cada Tray# se le asigna un ciclo for para que realice la trayectoria establecida.
#----------------------------
    for q in Tray1.y:
         #print(q)
         robot.q=q
         env.step(0.1)
#----------------------------
    for q in Tray2.y:
         #print(q)
         robot.q=q
         env.step(0.1)
#----------------------------
    for q in Tray3.y:
         #print(q)
         robot.q=q
         env.step(0.1)
#----------------------------
    for q in Tray4.y:
         #print(q)
         robot.q=q
         env.step(0.1)
#----------------------------
    for q in Tray5.y:
         #print(q)
         robot.q=q
         env.step(0.1)
#----------------------------

#----------------------------
    # return to home
    env.reset()
#----------------------------

# Aplicación de este robot
## Un brazo robótico para ayudar en la clasificación en almacenes logísticos
![](https://blog.seur.com/wp-content/uploads/2019/12/righthand_background.jpg)
Algunas de las opciones que se plantean para nuestro robot son las labores habituales de clasificación de objetos y paquetes en una cadena con agilidad y sin descanso. Los sectores más habituales en los que se aplica incluyen todo tipo de tiendas de ecommerce, el sector farmacéutico, de alimentación, productos de belleza, ropa y similares. En algunas instalaciones muchos de estos brazos trabajan en conjunto de forma coordinada, clasificando y empaquetando objetos en cajas, bandejas de cintas transportadores o **sobre robots móviles** que luego los transportan de un lugar a otro.

Finalmente podemos ver nuestro robot realizando las trayectorias que se explicaron anteriormente. [Funcionamiento ](https://www.youtube.com/watch?v=VfdWAtEAbjU "Funcionamiento ")

# Construcción paso a paso del robot 

en el siguiente link podrá observar mediante imágenes la construcción de nuestro robot.
[ConstrucciónRobot](https://robotmetalico.blogspot.com/ "ConstrucciónRobot")