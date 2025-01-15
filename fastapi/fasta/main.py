from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from api.shou.shou_app import shou_app as shou
from api.fu.fu_app import fu_app as fu
from api.rizhi.rizhi import rizhi_app as rizhi
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(shou,prefix="/shou",tags=["shou"])
app.include_router(fu,prefix="/fu",tags=["fu"])
app.include_router(rizhi,prefix="/rizhi",tags=["rizhi"])


@app.get("/file",tags=["file"])
def add_file(request: Request):

    return templates.TemplateResponse(
        "file.html",
        {
            "request": request,
        },
    )
@app.get("/",tags=["file"])
def first(request: Request):

    return templates.TemplateResponse(
        "first.html",
        {
            "request": request,
        },
    )


# 假设 app 是一个 FastAPI 应用实例
register_tortoise(
    app=app,  # 将 Tortoise ORM 注册到 FastAPI 应用实例上
    config=TORTOISE_ORM,  # 使用 TORTOISE_ORM 字典作为配置项来初始化 Tortoise ORM
    generate_schemas=True,  # 可选：如果需要在应用启动时自动生成数据库模式，请取消此行注释,如果数据库为空，则自动生成对应表单，生产环境不要开
#     # add_exception_handlers=True,  # 可选：添加异常处理器以处理 Tortoise ORM 引发的异常 生产环境不要开，会泄露调试信息
)


if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)