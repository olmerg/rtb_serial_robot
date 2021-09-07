"""
Created on Wed Feb 17 06:12:26 2021

please install pySerial
pip install pyserial

@author: olmer
"""
import numpy as np
import roboticstoolbox as rtb
import time
import serial
from math import pi

from roboticstoolbox.backends.Swift import Swift

class Swift_serial(Swift):  # pragma nocover
    """
    Graphical and Hardware backend using Serial_Swift

    This class connect to arduino through serial port and sent with the next protocol the movement to the motors:     
     - an alphabet value of th motor(ab,b,c,d,e or g) in lower case to decrement one degree or in upper case to increase one degree
     - sent h to return to home the robot (applied in the moment to add the robot or to reset the enviroment)

    **Note** You require to add install pySerial to use this library `pip install pyserial`

    Example:

    .. code-block:: python
        :linenos:
        from Swift_serial import Swift_serial
        env.add(robot)  #this return to home the robot
        # generate a trajetory
        qt = rtb.tools.trajectory.jtraj(np.array([0, 0, 0, 0,0, 0]), np.array([pi/2,0, pi/2, pi/2,pi/2, 0]), 20)
        for q in qt.y:
            print(q)
            robot.q=q
            env.step(0.1)
        # return to home
        env.reset()



    """
    def __init__(self, port,baudrate, display=True):
        """
        

        Parameters
        ----------
        port : TYPE Serial com to communicate with arduino
            DESCRIPTION.
        baudrate : TYPE
            DESCRIPTION.  baudrate 
        display : TYPE, optional
            DESCRIPTION. The default is True.

        Returns
        -------
        None.

        """
        super(Swift_serial, self).__init__()
        print('init serial ',port,' speed ',baudrate)
        self.serial=serial.Serial(timeout=1)
        self.serial.baudrate = baudrate
        self.serial.port = port
        self.serial.open()
        time.sleep(0.5)
        self.last_time = time.time()
        self.q_1=None

    def add(
            self, ob, show_robot=True, show_collision=False,
            readonly=False):
        super().add(ob,show_robot=show_robot,show_collision=show_collision,readonly=readonly)
        #TODO: verify the correct robot
        self.robots=[]
        self.robots.append(self.swift_objects[0])
        self.robots[-1].q=0*self.robots[-1].q
        self.q_1=self.robots[-1].q
        self.serial.write(b'h')
        
    
    def reset(self):
        """
        Reset the graphical scene and move to home the robot

        ``env.reset()`` triggers a reset of the 3D scene in the Swift window
        referenced by ``env``. It is restored to the original state defined by
        ``launch()``.

        """

        super().reset
        self.robots[-1].q=0*self.robots[-1].q
        self.q_1=self.robots[-1].q
        self.serial.write(b'h')
        self.step(0.01)

    def step(self, dt=0.05):
        """
        

        Parameters
        ----------
        dt : TYPE, optional
            DESCRIPTION. The default is 0.05.

        Returns
        -------
        None.

        """
        super().step(0.01)
        for robot_object in self.robots:
            robot = robot_object

            if self.swift_options[0]["readonly"] or robot.control_type == 'p':
                pass            # pragma: no cover

            elif robot.control_type == 'v':
                # this is made in swift class
                # for i in range(robot.n):
                #     q_1=self.q_1[i]
                #     robot.q[i] += robot.qd[i] * (dt)

                #     if np.any(robot.qlim[:, i] != 0) and \
                #             not np.any(np.isnan(robot.qlim[:, i])):
                #         robot.q[i] = np.min([robot.q[i], robot.qlim[1, i]])
                #         robot.q[i] = np.max([robot.q[i], robot.qlim[0, i]])
                move=np.round((robot.q-self.q_1)*180.0/pi)
                print(move)
                if(np.sum(np.abs(move))>0):
                        self.move_serial(move)
                line=self.serial.readline().decode("utf-8")
                if len(line)>0:
                    if line[0]=='*' and line[-3]=='*':
                        print(line[1:-3].split(','))
                #TODO: what to do if the motor did not come to the expected value?
                self.q_1=robot.q
                

            elif robot.control_type == 'a':
                pass

            else:            # pragma: no cover
                # Should be impossible to reach
                raise ValueError(
                    'Invalid robot.control_type. '
                    'Must be one of \'p\', \'v\', or \'a\'')
        
        #just wait if take small time
        time_taken = (time.time() - self.last_time)
        diff = dt - time_taken

        if diff > 0:
            time.sleep(diff)

        self.last_time = time.time()
    def move_serial(self,q_move):
        '''
        the protocol is one letter for each degree of movement of robot
        example first motor use a(-1) or A(+1)
        
         chr(ord(a)+1)
        '''
        comandos=''
        for move,i in zip(q_move,range(0, len(q_move))):
            command=65
            if move>0:
                for j in range(0,int(move)):
                    #self.serial.write(char(command+i))
                    comandos+=chr(command+i)
            elif move<0:
                for j in range(int(move),0):
                    #self.serial.write(b'S')
                    comandos+=chr(command+i+32)
        self.serial.write(comandos.encode())
        # if True:
        #     command=65+i #A is the motor zero+ and a is motor zero-
        #     if move>0:
        #         for j in range(0,move):
        #             self.serial.write(chr(command).encode())
        #             #print(chr(command+i))
        #             time.sleep(0.001)
        #     elif move<0:
        #         for j in range(move,0):
        #             self.serial.write(chr(command+32).encode())
        #             time.sleep(0.001)