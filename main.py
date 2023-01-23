from fastapi import FastAPI
from pydantic import BaseModel
import json
import requests
app = FastAPI(title="API", description="ЧТО ТО ДЕЛАЕТ")
url = 'https://card.wb.ru/cards/detail?nm={id}'


class Product(BaseModel):
    id : int
    name: str
    brand: str
    sale: int
    priceU:int
    salePriceU: int
    rating: int


def get_item(id:int):
    return requests.get(f"https://card.wb.ru/cards/detail?nm={id}").text


@app.get('/get-Product/{id}')
async def get_product(id:int):
    return json.loads(get_item(id))
