from fastapi import FastAPI

import uvicorn

from apps.app01.app01 import app01
from apps.app02.app02 import app02

app = FastAPI()

app.include_router(app01,prefix="/app01",tags=["get"])
app.include_router(app02,prefix="/app02",tags=["post"])

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)