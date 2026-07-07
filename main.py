from fastapi import FastAPI

app = FastAPI()

items = [
    {"id": 1, "name": "Projector", "status": "available"},
    {"id": 2, "name": "Chess Set", "status": "missing pieces"},
    {"id": 3, "name": "Button Maker", "status": "available"},
    {"id": 4, "name": "Ninja Creami", "status": "new"}

]

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
        if item[id] == item_id:
            return item
    
    return {"error": "Item not found"}