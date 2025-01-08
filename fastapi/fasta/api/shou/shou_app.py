from fastapi import APIRouter,UploadFile,Request,Response
import os,asyncio
from typing import List
# from models import Utr,Shou
from typing import Union,Optional
from fastapi.responses import JSONResponse
from datetime import datetime
from models import DaiShou,excel_data,Shou_model,RiZhi
from tortoise.queryset import Q
from fastapi.templating import Jinja2Templates


# from tortoise import Tortoise, fields, run_async


shou_app = APIRouter()
templates = Jinja2Templates(directory="templates")
filr_path = "api/shou/代收"

async def insert_sql(data,data_day):
    data = [Shou_model(**data_json) for data_json in data]

    await DaiShou.bulk_create(data)
    await RiZhi.create(card_id=str(data[0].card_id),date_day=str(data_day),date_time=str(data[0].date_time),status = "代收成功")

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
async def shou_time(request: Request,card_id : Optional[str] = None,date_time : Optional[str] = None,utr_id : Optional[str] = None):
    #查询条件
    if card_id == None and date_time == None and utr_id == None:
        data = await DaiShou.all()# 查询所有数据 QuerySet: 查询集
        print(data[0].date_time)
        return templates.TemplateResponse(
            "shou.html",
            {"data_list": data,
             "request": request,
             }
        )
    elif utr_id != None:
        data_utr = await DaiShou.filter(
            utr__icontains=utr_id
        )
        # print(data_utr[0].AA1)
        return templates.TemplateResponse(
            "shou.html",
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
        data = await DaiShou.filter(query)
        return templates.TemplateResponse(
            "shou.html",
            {"data_list": data,
             "request": request,
             }
        )
#根据utr进行查询
@shou_app.get("/utr/{utr_id}")
async def shou_utr_id(request: Request,utr_id : str = None):
    if utr_id == None:
        return templates.TemplateResponse(
        "shou.html",
        {
            "request": request,
        },
    )
    else:
        data_utr = await DaiShou.filter(
            utr__icontains=utr_id
        )
        # print(data_utr[0].AA1)
        return data_utr
@shou_app.get("/")
async def shou(request: Request):
    return templates.TemplateResponse(
        "shou.html",
        {
            "request": request,
        },
    )
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
        if file_name.endswith(".xlsx"):
            excel_data.xlsx_revise(file_path,file_name)
        elif file_name.endswith(".xls"):
            excel_data.xls_revise(file_path,file_name)
        elif file_name.endswith(".csv"):
            excel_data.csv_revise(file_path,file_name)
    for file_name in name_list:
        try:
            if file_name.endswith(".xlsx"):
                data_shou,data_day = excel_data.excel_read_data(file_path,file_name)
                # print('.......................................')
                await insert_sql(data_shou,data_day)
                os.remove(file_path+"/"+file_name)
        except:
            file_name = file_name.split('.')[0].split('-')
            await RiZhi.create(card_id=str(file_name[0])+str(file_name[1]),date_day=str(file_name[1]),date_time = str(datetime.now()),status = "代收失败")

    return {
        "data": '代收写入完成'
        }
    # data = excel_data().excel_read_data()
    # data : Union[str,List[Shou_model]]

    #单条插入
    # await DaiShou.create(utr="123",card_id="123",date_time="123")
    # await DaiShou.bulk_create()
    # return {
    #     "aaa": "插入成功"
    #     }

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
    # templates = Jinja2Templates(directory="templates")
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
