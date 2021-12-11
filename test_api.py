import requests
import json



def main():
    url = 'http://127.0.0.1:8000/item/'
    body = {
        "name": "帽子",
        "description": "blue hat",
        "price": 1000,
        "tax": 1.1
        }
    print(type(body))
    res = requests.post(url, json.dumps(body))
    print(f"json.dump{type(json.dumps(body))}")
    print(res)
    print(res.json())

if __name__ == "__main__":
    main()