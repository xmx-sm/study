from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from shou.shou_app import app as shou
from fu.fu_app import app as fu
import uvicorn
from Sqllog import TORTOISE_ORM
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(shou,prefix="/shou",tags=["shou"])
app.include_router(fu,prefix="/fu",tags=["fu"])

@app.get("/file")
def add_file(request: Request):

    return templates.TemplateResponse(
        "file.html",
        {
            "request": request,
        },
    )



# 假设 app 是一个 FastAPI 应用实例
register_tortoise(
    app=app,  # 将 Tortoise ORM 注册到 FastAPI 应用实例上
    config=TORTOISE_ORM,  # 使用 TORTOISE_ORM 字典作为配置项来初始化 Tortoise ORM
    # generate_schemas=True,  # 可选：如果需要在应用启动时自动生成数据库模式，请取消此行注释
    # add_exception_handlers=True,  # 可选：添加异常处理器以处理 Tortoise ORM 引发的异常
)

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)