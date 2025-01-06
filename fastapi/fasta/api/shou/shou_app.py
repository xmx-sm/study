from fastapi import APIRouter,UploadFile,Request,Response
import os,asyncio
from typing import List
# from models import Utr,Shou
from typing import Union,Optional
from fastapi.responses import JSONResponse
from datetime import datetime
from models import DaiShou,excel_data,Shou_model
from tortoise.queryset import Q
from fastapi.templating import Jinja2Templates

# from tortoise import Tortoise, fields, run_async


shou_app = APIRouter()

filr_path = "api/shou/代收"

async def insert_sql(data):
    data = [Shou_model(**data_json) for data_json in data]

    await DaiShou.bulk_create(data)
@shou_app.post("/add/file")
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
#查询相关操作
#根据时间，卡号查询
@shou_app.get("/check")
async def shou_time(card_id : Optional[str] = None,date_time : Optional[str] = None):
    #查询条件
    if card_id == None and date_time == None:
        data = await DaiShou.all()# 查询所有数据 QuerySet: 查询集
        print(data[0].date_time)
        return {"aaa": data}
    else:
        conditions_check = []
        if card_id != None:
            conditions_check.append(Q(card_id__icontains=card_id))
        if date_time != None:
            conditions_check.append(Q(date_time__icontains=date_time))
        query = Q()
        for condition in conditions_check:
            query &= condition
        data = await DaiShou.filter(query)
        return {"date": data}

#根据utr进行查询
@shou_app.get("/utr/{utr_id}")
async def shou_utr_id(utr_id : str):
    data_utr = await DaiShou.filter(
        utr__icontains=utr_id
    )
    return {
        "aaa": data_utr
        }
#插入数据
# @shou_app.post("/")
# async def shou_add(data : Union[str,List[Shou_model]] = None):
#     #单条插入
#     # await DaiShou.create(utr="123",card_id="123",date_time="123")
#     # await DaiShou.bulk_create()
#     return {
#         "aaa": "插入成功"
#         }
@shou_app.get("/insert")
async def shou_insert():
    file_path = "api/shou/代收"
    name_list = os.listdir(file_path)
    list_list = []
    for file_name in name_list:
        # print(file_name)
        if file_name.endswith(".xlsx"):
            pass
        elif file_name.endswith(".xls"):
            pass
            # excel_data.xls_revise(file_path,file_name)
        elif file_name.endswith(".csv"):
            excel_data.csv_revise(file_path,file_name)
    for file_name in name_list:
        if file_name.endswith(".xlsx"):
            # print(file_name)
            data_shou = excel_data.excel_read_data(file_path,file_name)
            await insert_sql(data_shou)
    return {
        "aaa": data_shou
        }
    # data = excel_data().excel_read_data()
    # data : Union[str,List[Shou_model]]

    #单条插入
    # await DaiShou.create(utr="123",card_id="123",date_time="123")
    # await DaiShou.bulk_create()
    return {
        "aaa": "插入成功"
        }

@shou_app.put("/{utr_id}")
async def shou_utr_put(utr_id : str):
    return {
        "aaa": "修改指定数据"
        }
@shou_app.delete("/{utr_id}")
def shou_utr_delete(utr_id : str):
    return {
        "aaa": "删除指定数据"
        }

@shou_app.get("/index")
async def getall(request : Request):
    templates = Jinja2Templates(directory="templates")
    data = await DaiShou.all()
    return templates.TemplateResponse(
        "测试.html",
        {
            "request": request,
            "data_utr": data
        },
    )



















# @app.get("/")
# async def shou_utr(request:Request,response:Response,utr : Optional[str] = None):
#     response.set_cookie(key="cookie", value=datetime.now())
#     if utr == None:
#         print("utr不能为空",utr)
#         return {"aaa": "utr不能为空",
#                 "cookie": request.cookies.get("cookie"),}
#     else:
#         print("utr",utr)
#         shou = await Shou.filter(A08=utr)
#         list_list = []
#         for i in shou:
#             list_list.append(f"{i.A08},{i.A01}")
#         return {"aaa": request.headers,
#                 "cookie": request.cookies,
#                 }
# @app.post("/")
# def shou_utr_post(utr : Utr):
#     print("utr",utr.utr)
#     if utr.utr == None:
#         print("utr不能为空",utr)
#         return {"aaa": "utr不能为空"}
#     else:
#         print("utr",utr.utr)
#         return {"aaa": utr.utr}
