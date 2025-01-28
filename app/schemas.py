from pydantic import BaseModel


class BookBase(BaseModel):
    name: str
    author: str
    price: int
    quantity: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id:int

    class Config:
        from_attributes = True
