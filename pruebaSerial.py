import time
import serial
#ffind serial port C:\Users\olmer\anaconda3\python -m serial.tools.list_ports

#print(serial.tools.list_ports)

ser = serial.Serial(timeout=1)
ser.baudrate = 115200
ser.port = 'COM4'
ser.open()
time.sleep(1)
if ser.isOpen():
    for i in range(0,100):
        line=ser.readline().decode("utf-8")
        if len(line)>0:
            if line[0]=='*' and line[-3]=='*':
                    print(line[1:-3].split(','))
        ser.write(b'a')
        time.sleep(0.1)
    ser.write(b'h')
    ser.close()
else:
    print("error")
