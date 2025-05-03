from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Item
from schemas import ItemCreate, ItemResponse
from database import SessionLocal, engine, Base
from fastapi.responses import FileResponse
import os

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory Management API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=ItemResponse, tags=["Inventory"])
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/", response_model=list[ItemResponse], tags=["Inventory"])
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

@app.get("/items/{item_id}", response_model=ItemResponse, tags=["Inventory"])
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=ItemResponse, tags=["Inventory"])
def update_item(item_id: int, updated_item: ItemCreate, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in updated_item.dict().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@app.delete("/items/{item_id}", tags=["Inventory"])
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"detail": "Item deleted successfully"}

@app.get("/", response_class=FileResponse)
def read_root():
    file_path = os.path.join("static", "index.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"message": "Welcome to Inventory Management API. Go to /docs for API documentation."}

