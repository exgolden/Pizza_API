from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]
    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "username":"isaibb",
                "email":"isai_alejandro@outlook.com",
                "password":"password",
                "is_staff":True,
                "is_active":True,
            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str="78e2fe2167428a6b636aeb082a920d6f00cdcaa906e19ff03cdbb51eb40b9eb"

class LogInModel(BaseModel):
    username:str
    password:str
    class Config:
        schema_extra={
            "example":{
                "username":"isaibb",
                "password":"password"
            }
        }

class OrderModel(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    pizza_size:Optional[str]="SMALL"
    user_id:Optional[int]
    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "quantity": 1,
                "pizza_size": "SMALL"
                }
        }

class OrderStatusModel(BaseModel):
    order_status:Optional[str]="PENDING"
    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "order_status":"PENDING"
            }
        }


