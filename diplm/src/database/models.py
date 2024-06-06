from typing import Optional
from pydantic import BaseModel

class BaseModelModify(BaseModel):
    id: Optional[int] = None

class Post(BaseModelModify):
    name: str
    power_level: int

class Personal(BaseModelModify):
    name: Optional[str] = None
    surname: Optional[str] = None
    post_id: int

class Users(BaseModelModify):
    login: str
    password: str
    personal_id: Optional[int]

class ClientData(BaseModelModify):
    name: Optional[str] = None
    surname: Optional[str] = None
    address: str
    phone_number: Optional[str] = None

class ItemType(BaseModelModify):
    name: str

class Item(BaseModelModify):
    name: str
    price: float
    type_id: int

class Deposit(BaseModelModify):
    item_id: int
    metal: Optional[str]= None
    test: Optional[str]
    item_weight: Optional[float] = None
    ClientData_id: int
    Personal_id: int

