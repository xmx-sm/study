from fastapi import APIRouter,UploadFile,Request
import os
from typing import List
# from models import Utr
from typing import Union,Optional
from fastapi.templating import Jinja2Templates

fu_app = APIRouter()
templates = Jinja2Templates(directory="fu/templates")

filr_path = "fu/代付"
# file_path = os.path.join("imgs", 'file.filename')
@fu_app.post("/add/file")
def fu_add_file(file_list: List[UploadFile]):
    file_list_name = []
    """上传文件"""
    for file in file_list:
        file_path = os.path.join(filr_path, file.filename)
        print(file_path)
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
@fu_app.get("/")
def fu_utr(request : Request,utr : Optional[str] = None,):
    if utr == None:
        return {"utr": "utr不能为空"}
    else:
        return templates.TemplateResponse(
            "utr.html",
            {
                "request": request,
                "utr": utr,
            },
        )
