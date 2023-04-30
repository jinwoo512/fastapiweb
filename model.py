from pydantic import BaseModel

# class PacktBook(BaseModel):
#     id: int
#     Name: str
#     Publishers: str
#     Isbn: str

# class Item (BaseModel):
#     item: str
#     status: str

class Todo(BaseModel):
    id: int
    item: str

