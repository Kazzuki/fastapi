from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field
from pydantic.errors import DateError

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
class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    # pydanticのvalidation機能をFastAPIが恩恵を得ている
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: List[Item]

@app.post("/item/")
async def create_item(item: Item):
    # return item
    return {"message": f"{item.name}は、税込価格{int(item.price * item.tax)}円です"}
# 引数が、リクエストボディになって、返り値がレスポンスボディになるのか？

@app.post("/")
async def index(date: Data):
    return {"data": date}

