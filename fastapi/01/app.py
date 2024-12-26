from fastapi import FastAPI
import uvicorn
 # 假设 app01 模块中定义了一个名为 router 的 APIRouter 实例
from apps.app01.app01 import router

# 创建主 FastAPI 应用实例
main_app = FastAPI()

# 包含来自 app01 模块的路由器，并添加路径前缀
main_app.include_router(router, prefix="/hello",tags=["hello","aa"])

if __name__ == '__main__':
    uvicorn.run(main_app, host='127.0.0.1', port=8000)