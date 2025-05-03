# schemas.py (Pydantic Schemas)
from pydantic import BaseModel, Field

class ItemCreate(BaseModel):  # For incoming request
    name: str
    quantity: int
    price: float

class ItemResponse(BaseModel):  # For outgoing response
    id: int
    name: str
    quantity: int
    price: float

    class Config:
        from_attributes = True

class Item(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)
