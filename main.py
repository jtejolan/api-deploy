from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

class Item(BaseModel):
    name:str
    status:str

items = [
    {"id": 1, "name": "Projector", "status": "available"},
    {"id": 2, "name": "Chess Set", "status": "missing pieces"},
    {"id": 3, "name": "Button Maker", "status": "available"},
    {"id": 4, "name": "Ninja Creami", "status": "new"}

]

@app.get("/version")
def version():
    return {
        "app": "basic-api",
        "version": "1.0.0"
    }


@app.get("/")
def home():
    return {"message": "My API is live"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}"}

@app.get("/new")
def new():
    return {"message": f"This is a new endpoint."}

@app.get("/items")
def get_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/search")
def search_items(q: str):
    results = []
    for item in items:
        if q.lower() in item["name"].lower():
            results.append(item)
    return results

@app.post("/items")
def add_item(item: Item):
    new_item = {
        "id": len(items) + 1,
        "name": item.name,
        "status": item.status,
    }

    items.append(new_item)
    return new_item