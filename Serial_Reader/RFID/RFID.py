import RFIDReader
import Database
import User
from time import sleep

rfidReader = RFIDReader.RFIDReader()
database = Database.Database()

while True:
    input = rfidReader.readFromSerial()
    user = database.findUserByRFID(input)
    if user != None:
        user.toString()
    sleep(0.1)