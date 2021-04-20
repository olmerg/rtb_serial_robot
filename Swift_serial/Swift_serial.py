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



class Swift_serial(rtb.backends.Swift):  # pragma nocover
    """
    Graphical backend using Serial_Swift

    Swift is a web app built on three.js. It supports many 3D graphical
    primitives including meshes, boxes, ellipsoids and lines. It can render
    Collada objects in full color.

    :param display: Do not launch the graphical front-end of the simulator.
        Will still simulate the robot. Runs faster due to not needing to
        display anything.
    :type display: bool

    Example:

    .. code-block:: python
        :linenos:

        import roboticstoolbox as rtb

        robot = rtb.models.DH.Panda()  # create a robot

        pyplot = rtb.backends.Swift()   # create a Swift backend
        pyplot.add(robot)              # add the robot to the backend
        robot.q = robot.qz             # set the robot configuration
        pyplot.step()                  # update the backend and graphical view



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
        super(Swift_serial, self).__init__(realtime=False)
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
        self.robots[-1]['ob'].q=0*self.robots[-1]['ob'].q
        self.q_1=self.robots[-1]['ob'].q
        self.serial.write(b'h')
        
    
    def reset(self):
        """
        Reset the graphical scene and move to home the robot

        ``env.reset()`` triggers a reset of the 3D scene in the Swift window
        referenced by ``env``. It is restored to the original state defined by
        ``launch()``.

        """

        super().reset
        self.robots[-1]['ob'].q=0*self.robots[-1]['ob'].q
        self.q_1=self.robots[-1]['ob'].q
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
        super().step(dt)
        for robot_object in self.robots:
            robot = robot_object['ob']

            if robot_object['readonly'] or robot.control_type == 'p':
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
        TODO: cambiar para el envio del comando de los 5 motores simultaneamente
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