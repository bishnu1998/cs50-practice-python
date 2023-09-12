import requests

def main():
    res = requests.get("https://www.google.com/form")
    print("hi")
    print(res.text)

if __name__=="__main__":
    main()