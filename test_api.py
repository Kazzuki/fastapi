import requests
import json

# main.pyのAPIをテストする
def main():
    url = 'http://127.0.0.1:8000/item/'
    body = {
        "name": "帽子帽子",
        "description": "blue hat",
        "price": 1000,
        "tax": 1.1
        }
    print(type(body))
    
    # 辞書型をjson形式に変えてリクエストボディに組み込む必要がある
    # jaonは辞書型の書き方をするけど、dic型ではなく、str型なので型変換(dicからのJson形式のstrに変換)が必要である
    res = requests.post(url, json.dumps(body))
    print(f"json.dump{type(json.dumps(body))}")
    print(res)
    print(res.json())

if __name__ == "__main__":
    main()