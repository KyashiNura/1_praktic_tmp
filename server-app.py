from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    location: str
    weight: float

mas = []

@app.get('/')
def read_root():
    return {"message": "Здесь могла быть ваша реклама"}

@app.post("/items/")
async def create_item(item: Item):
    mas.append(item)
    return {"message": "Item created", "item": item}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if 0<=item_id <len(mas):
        return {"item": mas[item_id]}
    return {"item_id": item_id, "query": q}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)