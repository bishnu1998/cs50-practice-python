from tech.helper.DBHelper import DBConnector

class UserDao(DBConnector):
    
    #inherate the database connection
    def __init__(self):
        super().__init__()
        self.cursor = self.con.cursor()

    #insert operation
    def insert_flights(self,origin,destination,duration):
        flag = False
        try:
            flight = "INSERT INTO flights(origin,destination,duration)VALUES('{}','{}',{})".format(origin,destination,duration)
            self.cursor.execute(flight)
            self.con.commit()
            #self.cursor.close()
            flag = True

        except:
            print("error!!")
        
        return flag
    
    #fetch operation
    def fetch_flights(self):
        flight = "SELECT*FROM flights"
        self.cursor.execute(flight)
        return self.cursor
    


    #Make sure the flight exist or not.
    def exist_flight(self,id):

        flag = False
        try:
            print("id:",type(id))
            flight ="SELECT*FROM flights WHERE id={}".format(id)
            self.cursor.execute(flight)
            flag = True
            if self.cursor is None:
                flag = False
                print("no flight exist!!!")


        except:
            print("error!!")

        return flag

    #book flight for passenger
    def flight_book(self,name,flight_id):
        flag = False
        try:
            query = "INSERT INTO passangers(NAME,flight_id)VALUES('{}',{})".format(name,flight_id)
            self.cursor.execute(query)
            self.con.commit()
            flag = True

        except:
            print("error in flight booking")
        
        return flag
    
    #fetch flight if id is given
    def fetch_flight_id(self,id):
        flight = "SELECT*FROM flights WHERE id={}".format(id)
        self.cursor.execute(flight)
        return self.cursor

    #get all passengers.
    def flight_passengers(self,flight_id):
        passengers = "SELECT NAME FROM passangers WHERE flight_id={}".format(flight_id)
        self.cursor.execute(passengers)
        return self.cursor


