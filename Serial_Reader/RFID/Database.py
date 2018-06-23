import mysql.connector
import User

class Database:
    """Connection to SQL database """
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(user="root",
                                                password="",
                                                host="localhost",
                                                database="logging")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Access denied")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def getAllUsers(self):
        cursor = self.conn.cursor()

        query = ("SELECT id, name, rfid_value FROM rfid")

        cursor.execute(query)

        for (id, name, lastname) in cursor:
            print (name)

    def findUserByRFID(self, rfid):
        cursor = self.conn.cursor();
        query = ("SELECT id, name FROM rfid WHERE rfid_value='{}'".format(rfid))
        cursor.execute(query)

        if cursor.rowcount != 0:
            for (id, name) in cursor:
                cursor.close()
                return User.User(id, name, rfid)
        else:
            cursor.close()
            return None

    def createUser(self, name, rfid):
        cursor = self.conn.cursor()
        #query = ("INSERT INTO rfid(name, rfid_value) VALUES(%(name)s, %(rfid_value)s")
        data = {
            "name" : name,
            "rfid_value" : rfid
        }

        query = ("INSERT INTO rfid(name, rfid_value) VALUES('{}', '{}')".format(name, rfid))

        #cursor.execute(query, data)
        cursor.execute(query)
        self.conn.commit()
        cursor.close()

    def __del__(self):
        self.conn.close()

