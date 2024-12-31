from fastapi import APIRouter,UploadFile,Request,Response
import os
from typing import List
from models import Utr,Shou
from typing import Union,Optional
from fastapi.responses import JSONResponse
from datetime import datetime
# from tortoise import Tortoise, fields, run_async


app = APIRouter()

filr_path = "shou/代收"
@app.post("/add/file")
def fu_add_file(file_list: List[UploadFile]):
    file_list_name = []
    """上传文件"""
    for file in file_list:
        file_path = os.path.join(filr_path, file.filename)
        with open(file_path, "wb") as f:
            # 写入文件 片段
            for file_fragment in file.file:
                f.write(file_fragment)
        file_list_name.append(file.filename)
    return {
        "code": 200,
        "msg": "上传成功",
        "data": file_list_name
    }

@app.get("/")
async def shou_utr(request:Request,response:Response,utr : Optional[str] = None):
    # response.set_cookie(key="cookie", value=datetime.now())
    if utr == None:
        print("utr不能为空",utr)
        return {"aaa": "utr不能为空"}
    else:
        print("utr",utr)
        shou = await Shou.filter(A08=utr)
        list_list = []
        for i in shou:
            list_list.append(f"{i.A08},{i.A01}")
        return {"aaa": str(list_list),
                }
# @app.post("/")
# def shou_utr_post(utr : Utr):
#     print("utr",utr.utr)
#     if utr.utr == None:
#         print("utr不能为空",utr)
#         return {"aaa": "utr不能为空"}
#     else:
#         print("utr",utr.utr)
#         return {"aaa": utr.utr}
