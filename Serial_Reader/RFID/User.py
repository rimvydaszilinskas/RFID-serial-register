class User:
    def __init__(self, id = None, name = None, rfid_value = None):
        self.id = id
        self.name = name
        self.rfid_value = rfid_value

    def toString(self):
        print("ID: {}".format(self.id))
        print("Name: " + self.name)
        print("RFID: " + self.rfid_value)