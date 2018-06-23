import serial
from time import sleep

class RFIDReader:
    def __init__(self):
        #start serial running at 9600bps
        self.ser = serial.Serial("COM3", 9600)

    def readFromSerial(self):
        input = self.ser.readline()
        input = input.rstrip()
        return input