from fastapi import FastAPI, Form
from request.product import *

app = FastAPI()


# path parameter
@app.get("/item/{id}")
async def item_id(id: int):
    return {"message": f"This item_id is {id}"}


# query parameter
@app.get("/user/product")
async def product(id: int, price: int, name: str | None = None):
    if name:
        return {"message": f"The product_id is {id} and it's price is {price} , brand name is {name} "}

    else:
        return {"message": f"The product_id is {id} and it's price is {price}"}


# request body parameter
@app.post("/product")
async def item_details(item: Item):
    item_new_key = item.dict()

    if item.price is not None and item.gst is not None:
        include_gst_price = item.price + item.gst
        item_new_key["gst_include_price"] = include_gst_price

    if "gst_include_price" in item_new_key:
        return item_new_key
    else:
        return "Not Present"


@app.post("/product/{product_id}")
def product_description(item: Item, user: User, product_id: int, product_name: str):
    return {"user": user, "product_id": product_id, "product_name": product_name, "item": item}


@app.post("/offer")
def product_des(product: Product):
    return {"product": product}


@app.post("/date")
def time_module(event: Event):
    return event


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
