from fastapi import FastAPI
from pydantic import BaseModel

class Date(BaseModel):
    x: float
    y: float

app = FastAPI()

@app.get('/')
def index():
    return{'message': 'hello world'}

@app.post('/')
def calc(date: Date):
    z = date.x * date.y
    return {'result': z}