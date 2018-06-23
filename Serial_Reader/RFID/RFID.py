import RFIDReader
import Database
import User
from time import sleep

rfidReader = RFIDReader.RFIDReader()
database = Database.Database()

while True:
    rfid_input = rfidReader.readFromSerial()
    
    user = database.findUserByRFID(rfid_input)
    if user != None:
        user.toString()
    else:
        print("No user registered.")
        user_input = input('Would you like to register a new card? (Y/N): ')
        if(user_input == "Y"):
            name = input("Enter name: ")
            database.createUser(name, rfid_input)
        else:
            continue
    sleep(0.1)