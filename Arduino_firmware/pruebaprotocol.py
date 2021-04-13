import time
import numpy as np
def move_serial(q_move):
        '''
        El protocolo consiste en enviar el numero de letras para la cantidad de grados del robot
        ejemplo el motor uno(hombro) es la letra a(-1) o la letra A(+1)
        
         chr(ord(a)+1)
        '''
        #print(i,move)
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
        print(comandos.encode())
            
        

if __name__ == '__main__':

    move_serial(np.array([5.5,5,5,5,5]))
    move_serial(np.array([-5,-5,-5,-5,-5]))

