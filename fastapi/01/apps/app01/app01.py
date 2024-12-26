from fastapi import APIRouter

router  = APIRouter()

@router .get("/")
async def read_root():
    return {"message": "Hello World"}
@router .get("/aa")
async def read_aa():
    return {"message": "Hello aa"}