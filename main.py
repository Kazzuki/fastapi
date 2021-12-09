from typing import Optional
from fastapi import FastAPI


app = FastAPI()

# @はデコレータと言われる
@app.get("/hello")
async def index():
    return {"message" : "Hello World"}

# パスパラメータ
@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {"message" : country_name}

# クエリパラメータ
@app.get("/anime")
async def anime(anime_name: str = "kauzki", anime_no: int = 1):
    return{
        "anime_name" : anime_name,
        "anime_no" : anime_no
    }

# 必須ではないオプションパラメータ
@app.get("/sushi")
async def sushi(sushi_name: Optional[str] = None, sushi_no: Optional[int] = None):
    return{
        "name" : sushi_name,
        "no" : sushi_no
    }
KA`UKI