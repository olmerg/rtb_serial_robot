import time
import serial
#ffind serial port C:\Users\olmer\anaconda3\python -m serial.tools.list_ports

#print(serial.tools.list_ports)

ser = serial.Serial()
ser.baudrate = 38400
ser.port = 'COM4'
ser.open()
time.sleep(1)
if ser.isOpen():
    for i in range(0,100):
        line=ser.readline()

        print(line.decode("utf-8").split(','))
        ser.write(b'R')
        time.sleep(0.1)
    ser.close()
else:
    print("error")
