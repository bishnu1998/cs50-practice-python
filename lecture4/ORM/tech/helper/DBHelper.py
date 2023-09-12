import mysql.connector as connector

class DBConnector:
    def __init__(self) :
        self.con = connector.connect(
            host = "localhost",
            user = "root",
            password ="",
            database="cs50",
            consume_results=True
        )
    
    def checkConnection(self):
        if self.con.is_connected:
            print("connection Successfull!!")
        else:
            print("connection error!!")



def main():
    db = DBConnector()
    db.checkConnection()

if __name__=="__main__":
    main()