import serial
from time import sleep

#register serial running at 9600bps
ser = serial.Serial("COM3", 9600)

while True:
    input = ser.readline()
    input = input.rstrip()
    print(input)
    sleep(0.1)
