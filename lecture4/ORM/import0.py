import csv
from tech.Dao.DBUser import UserDao
help1 = UserDao()
def main():

    try:
        with open("flights.csv","r") as f:
            reader = csv.reader(f)
            
            for row in reader:
                print("i am csv;;")
                flag = help1.insert_flights(row[0],row[1],int(row[2]))
                if flag:
                    print("successfull inserted!!")
            
    except:
        print("error occure in insertion of flights!!")

if __name__=="__main__":
    main()