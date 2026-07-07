from fastapi import FastAPI

app = FastAPI()

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
def new(name: str):
    return {"message": f"This is a new endpoint."}