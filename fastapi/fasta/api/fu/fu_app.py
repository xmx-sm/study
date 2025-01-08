# from fastapi import APIRouter,UploadFile,Request
# import os
# from typing import List
# # from models import Utr
# from typing import Union,Optional
# from fastapi.templating import Jinja2Templates

# fu_app = APIRouter()
# templates = Jinja2Templates(directory="fu/templates")

# filr_path = "fu/代付"
# # file_path = os.path.join("imgs", 'file.filename')
# @fu_app.post("/add/file")
# def fu_add_file(file_list: List[UploadFile]):
#     file_list_name = []
#     """上传文件"""
#     for file in file_list:
#         file_path = os.path.join(filr_path, file.filename)
#         print(file_path)
#         with open(file_path, "wb") as f:
#             # 写入文件 片段
#             for file_fragment in file.file:
#                 f.write(file_fragment)
#         file_list_name.append(file.filename)
#     return {
#         "code": 200,
#         "msg": "上传成功",
#         "data": file_list_name
#     }
# @fu_app.get("/")
# def fu_utr(request : Request,utr : Optional[str] = None,):
#     if utr == None:
#         return {"utr": "utr不能为空"}
#     else:
#         return templates.TemplateResponse(
#             "utr.html",
#             {
#                 "request": request,
#                 "utr": utr,
#             },
#         )
from fastapi import APIRouter,UploadFile,Request,Response
import os,asyncio
from typing import List
# from models import Utr,Shou
from typing import Union,Optional
from fastapi.responses import JSONResponse
from datetime import datetime
from models import DaiFu,excel_data,Fu_model,RiZhi
from tortoise.queryset import Q
from fastapi.templating import Jinja2Templates

# from tortoise import Tortoise, fields, run_async


fu_app = APIRouter()
templates = Jinja2Templates(directory="templates")
filr_path = "api/fu/代付"

async def insert_sql(data,data_day):
    data = [Fu_model(**data_json) for data_json in data]

    await DaiFu.bulk_create(data)
    await RiZhi.create(card_id=str(data[0].card_id),date_day=str(data_day),date_time=str(data[0].date_time),status = "代付成功")
@fu_app.get("/")
async def fu(request: Request):
    return templates.TemplateResponse(
        "fu.html",
        {
            "request": request,
        },
    )
@fu_app.post("/add/file")
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
@fu_app.get("/check")
async def fu_time(request: Request,card_id : Optional[str] = None,date_time : Optional[str] = None,utr_id : Optional[str] = None):
    #查询条件
    if card_id == None and date_time == None and utr_id == None:
        data = await DaiFu.all()# 查询所有数据 QuerySet: 查询集
        print(data[0].date_time)
        return templates.TemplateResponse(
            "fu.html",
            {"data_list": data,
             "request": request,
             }
        )
    elif utr_id != None:
        data_utr = await DaiFu.filter(
            utr__icontains=utr_id
        )
        # print(data_utr[0].AA1)
        return templates.TemplateResponse(
            "fu.html",
            {
                "request": request,
                "data_list": data_utr
            },
        )
    else:
        conditions_check = []
        if card_id != None:
            conditions_check.append(Q(card_id__icontains=card_id))
        if date_time != None:
            conditions_check.append(Q(date_time__icontains=date_time))
        query = Q()
        for condition in conditions_check:
            query &= condition
        data = await DaiFu.filter(query)
        return templates.TemplateResponse(
            "fu.html",
            {"data_list": data,
             "request": request,
             }
        )
#根据utr进行查询
@fu_app.get("/utr/{utr_id}")
async def fu_utr_id(request: Request,utr_id : str = None):
    if utr_id == None:
        return templates.TemplateResponse(
        "fu.html",
        {
            "request": request,
        },
    )
    else:
        data_utr = await DaiFu.filter(
            utr__icontains=utr_id
        )
        # print(data_utr[0].AA1)
        return data_utr

@fu_app.get("/insert")
async def fu_insert():
    file_path = "api/fu/代付"
    name_list = os.listdir(file_path)
    list_list = []
    for file_name in name_list:
        if file_name.endswith(".xlsx"):
            excel_data.xlsx_revise(file_path,file_name)
        elif file_name.endswith(".xls"):
            excel_data.xls_revise(file_path,file_name)
        elif file_name.endswith(".csv"):
            excel_data.csv_revise(file_path,file_name)
    for file_name in name_list:
        try:
            if file_name.endswith(".xlsx"):
                data_fu,data_day = excel_data.excel_read_data(file_path,file_name)
                # print(data_fu[55])
                await insert_sql(data_fu,data_day)
                os.remove(file_path+"/"+file_name)
        except:
            file_name = file_name.split('.')[0].split('-')
            await RiZhi.create(card_id=str(file_name[0])+str(file_name[1]),date_day=str(file_name[1]),date_time = str(datetime.now()),status = "代付失败")

    return {
        "aaa": '代付写入完成'
        }


@fu_app.put("/{utr_id}")
async def fu_utr_put(utr_id : str):
    return {
        "aaa": "修改指定数据"
        }
@fu_app.delete("/{utr_id}")
def fu_utr_delete(utr_id : str):
    return {
        "aaa": "删除指定数据"
        }







