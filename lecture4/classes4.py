class Flight:
    counter =1
    def __init__(self,origin,destination,duration):
         
         #keep track of id.
         self.id = Flight.counter
         Flight.counter +=1

         #keep track of passengers.
         self.passengers = []

         #details about flights
         self.origin = origin
         self.destination = destination
         self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

        print()
        print("Passengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")
        
    def delay(self,amount):
        self.duration +=amount
    
    def add_passenger(self,p):
        self.passengers.append(p)
        p.flight_id = self.id


#Passenger class
class Passenger:
    def __init__(self,name):
        self.name = name
    

def main():
    #create flight.
    f1 = Flight(origin="New York",destination="Paris",duration=450)

    #create passengers
    alice = Passenger(name="Alice")
    bob = Passenger(name="Bob")

    #add passengers.
    f1.add_passenger(alice)
    f1.add_passenger(bob)

    f1.print_info()
    

if __name__=="__main__":
    main()


