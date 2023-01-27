from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
import json
import requests
from typing import Union, List, Tuple
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
    provider: str
    supplierId:int
    def a(self):
      pass
d = {
  "state": 0,
  "params": {
    "curr": "rub",
    "version": 1
  },
  "data": {
    "products": [
      {
        "id": 19496870,
        "root": 14453504,
        "kindId": 0,
        "subjectId": 667,
        "subjectParentId": 657,
        "name": "Машинка для удаления катышков Mijia Rechargeable Lint Remove…",
        "brand": "Xiaomi",
        "brandId": 19467,
        "siteBrandId": 29467,
        "supplierId": 99452,
        "sale": 50,
        "priceU": 170000,
        "salePriceU": 85000,
        "logisticsCost": 0,
        "extended": {
          "basicSale": 50,
          "basicPriceU": 85000
        },
        "pics": 5,
        "rating": 5,
        "feedbacks": 13966,
        "panelPromoId": 152183,
        "promoTextCard": "КИБЕР НЕДЕЛЯ",
        "promoTextCat": "КИБЕР НЕДЕЛЯ",
        "volume": 7,
        "colors": [],
        "promotions": [
          63484,
          66925,
          79972,
          84211,
          92742,
          96213,
          98660,
          133413,
          137206,
          139114,
          151180,
          151424,
          152095,
          152139,
          152183,
          152530
        ],
        "sizes": [
          {
            "name": "",
            "origName": "0",
            "rank": 0,
            "optionId": 51923440,
            "stocks": []
          }
        ],
        "diffPrice": False
      }
    ]
  }
}


def get_item(id:int):
    return json.loads(
        requests.get(f"https://card.wb.ru/cards/detail?nm={id}").text)


def get_data(l:list, data: dict):
  result = {}
  for key in l:
    a = data["data"]["products"][0].get(key)
    result.update({key: a})
  return result



@app.get('/get-Product/{item_id}')
async def get_product(params: Union[List[str], None] = Query(default=None), item_id:int = Path()):
  return get_data(params, get_item(item_id))


@app.get("/items/")
async def read_items(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items



c = ('19496870', [
  "brand",
  "feedbacks",
  "name",
  "priceU"
  ], ["brand",   "feedbacks",   "name",   "priceU"])


@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
  print()
  results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
  if q:
    results.update({"q": q})
  return results