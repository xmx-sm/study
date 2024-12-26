from fastapi import APIRouter
from pydantic import BaseModel,Field,validator
from typing import List,Union


app02 = APIRouter()

class Item(BaseModel):
    name: str
    age: int =Field(None,gt=0)#加限制
    other : Union[str,int,None] = None #可空
    id: str = None
    list_1 : List[str] = []
class Item2(BaseModel):
    name2: str
    age2: int =Field(None,gt=0)#加限制
    other2 : Union[str,int,None] = None #可空
    id2: str = None
    list_2 : List[str] = []
    clsss : Item
class Data(BaseModel):
    data:List[Item2] #传入列表

@app02.post("/")
def read_root():
    return {"Hello": "World"}

@app02.post("/aa")
def aa(data : Item):
    print(data)
    print(data.dict())
    return data
@app02.post("/bb")
def bb(data : Item2):
    print(data)
    print(data.dict())
    return data

@app02.post("/cc1")
def cc1(data : Data):
    return data