from fastapi import FastAPI, Path
from typing import Optional


app = FastAPI()

inventory={
    1:{
        "name":"MILK",
        "price":3.99,
        "brand":"Reular"
    },
    2:{
        "name":"chocomilk",
        "price":4.77,
        "brand":"diet"
    }
}


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None,description="The ID of the item you love")):
    return inventory[item_id]


