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
                return User.User(id, name, rfid)
        else:
            return None

    #def __del__(self):
        #self.conn.close()

