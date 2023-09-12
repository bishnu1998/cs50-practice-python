import requests

def main():
    res = requests.get("http://127.0.0.1:8080/api/flights/1")
    if res.status_code !=200:
        raise Exception("ERROR: API request unsuccessful!")
    data =res.json()
    print(data)

if __name__=="__main__":
    main()
