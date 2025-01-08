from fastapi import APIRouter,UploadFile,Request,Response
import os,asyncio
from typing import List
# from models import Utr,Shou
from typing import Union,Optional
from fastapi.responses import JSONResponse
from datetime import datetime
from models import RiZhi
from tortoise.queryset import Q

rizhi_app = APIRouter()
@rizhi_app.get("/check")
async def shou_time(card_id : Optional[str] = None,date_day : Optional[str] = None):
    #查询条件
    if card_id == None and date_day == None:
        data = await RiZhi.all()# 查询所有数据 QuerySet: 查询集
        print(data[0].date_time)
        return {"data": data}
    else:
        conditions_check = []
        if card_id != None:
            conditions_check.append(Q(card_id=card_id))
        if date_day != None:
            conditions_check.append(Q(date_day=date_day))
        query = Q()
        for condition in conditions_check:
            query &= condition
        data = await RiZhi.filter(query)
        return {"date": data}