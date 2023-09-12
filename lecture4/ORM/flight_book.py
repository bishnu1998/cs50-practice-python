from flask import Flask,render_template,request,jsonify
from tech.Dao.DBUser import UserDao

helper1 = UserDao()

app =Flask(__name__,template_folder='template')

@app.route('/')
def index():

    #to show in option
    flights = helper1.fetch_flights()
    return render_template("flight_index.html",flights=flights)

@app.route('/book',methods=["POST"])
def book():
    """book a flight"""
    #get form information
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
        print("name:",name)
        print("flight_id:",flight_id)
        print("type:",type(flight_id))
    except ValueError:
        return render_template("flight_error.html",msg="invalid number")

     #Make sure the flight exists or not.
    flag = helper1.exist_flight(flight_id)
    print("flag1:",flag)
    if flag == False:
        msg = "No flight exist!"
        return render_template("flight_error.html",msg=msg)

    #if flight exist book flight 
    flag = helper1.flight_book(name,flight_id)
    print("flag2:",flag)
    if flag:
        msg = "successfully booked the flight"
        return render_template("flight_success.html",msg=msg)
    
    msg = "Error on Booking!"
    return render_template("flight_error.html",msg=msg)




@app.route('/flights')
def flights():
    """List all Flights."""
    flights = helper1.fetch_flights()
    return render_template("flight_flight.html",flights=flights)


@app.route('/flight/<int:flight_id>')
def flight(flight_id):
    
    #make sure flight exists or not.
    flights=[]
    flight = helper1.fetch_flight_id(flight_id)
    for i in flight:
        flights.append(i)
    if flight is None:
        return render_template("flight_error.html",msg="flight doesnot exits!!")
    

    #get all passengers
    passenger=[]
    passengers = helper1.flight_passengers(flight_id)
    for p in passengers:
        passenger.append(p)
    return render_template("flight.html",passengers=passenger,flights=flights)


@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    """Return details about flight."""

    #Make sure flight exists.

    flight1=helper1.fetch_flight_id(flight_id)
    
    if flight1 is None:
        return jsonify({"error":"invalid flight_id"}),422
    for j in flight1:
        dict = {'origin':j[1],'destination':j[2],'duration':j[3]}

    passengers = helper1.flight_passengers(flight_id)
    #update the dictionary by name
    pas=[]
    for i in passengers:
        print(i)
        pas.append(i)
        
    #dict['name']=pas
    return jsonify({
        "origin":dict['origin'],
        "destination":dict['destination'],
        "duration":dict['duration'],
        "passangers":pas
    })
            



if __name__=="__main__":
    app.run(debug=True,port=8080)