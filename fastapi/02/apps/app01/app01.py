from fastapi import APIRouter

app01 = APIRouter()

@app01.get("/")
def aa():
    return {"message": "Hello World"}

# @app01.get("/{id}")
# def bb(id: str = None):
#     return {"id": id}

@app01.get("/{id}/{name}")
def cc2(id: str = None, name: str = None):
    return {"id": id, "name": name}

@app01.get("/{id}")
def cc1(id: str = None, name: str = None,age: int = None):
    return {"id": id, "name": name,"age" :age}