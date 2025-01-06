from tortoise import Model
from tortoise import fields #字段
from typing import Union, Optional,List
from pydantic import BaseModel, Field
import pandas as pd,json
# class excel(BaseModel):
#     birth: Union[str, None] = None
#     friends: List[int] = []
#     description: Optional[str] = None

class excel_name():
    def xlsx_revise(file_path,file_name):
        print(file_path)
        df = pd.read_excel(str(file_path) + '/' + str(file_name))
        old_name = df.columns.to_list()
        new_name = {}
        for i in range(len(old_name)):
            new_name[old_name[i]] = "AA"+str(i)
        df.rename(columns=new_name,inplace=True)
        df.to_excel(file_path,index=False)
    def csv_revise(file_path,file_name):
        df = pd.read_csv(str(file_path) + '/' + str(file_name))
        old_name = df.columns.to_list()
        new_name = {}
        for i in range(len(old_name)):
            new_name[old_name[i]] = "AA"+str(i)
        df.rename(columns=new_name,inplace=True)
        file_new_name = str(file_name).split('.')[0] + '.xlsx'
        df.to_excel(str(file_path) + '/' + str(file_new_name),index=False)
    def xls_revise(file_path,file_name):
        df = pd.read_excel(str(file_path) + '/' + str(file_name), engine='xlrd')
        old_name = df.columns.to_list()
        new_name = {}
        for i in range(len(old_name)):
            new_name[old_name[i]] = "AA"+str(i)
        df.rename(columns=new_name,inplace=True)
        file_new_name = str(file_name).split('.')[0] + '.xlsx'
        df.to_excel(str(file_path) + '/' + str(file_new_name),index=False)


class DaiShou(Model):
    id = fields.IntField(pk=True,description='id')
    utr = fields.TextField(description='utr',null=True, default=None)
    date_time = fields.TextField(description='date_time',null=True, default=None)
    card_id = fields.TextField(description='card_id',null=True, default=None)
    AA1 = fields.TextField(null=True, default=None)
    AA2 = fields.TextField(null=True, default=None)
    AA3 = fields.TextField(null=True, default=None)
    AA4 = fields.TextField(null=True, default=None)
    AA5 = fields.TextField(null=True, default=None)
    AA6 = fields.TextField(null=True, default=None)
    AA7 = fields.TextField(null=True, default=None)
    AA8 = fields.TextField(null=True, default=None)
    AA9 = fields.TextField(null=True, default=None)
    AA10 = fields.TextField(null=True, default=None)
    AA11 = fields.TextField(null=True, default=None)
    AA12 = fields.TextField(null=True, default=None)
    AA13 = fields.TextField(null=True, default=None)
    AA14 = fields.TextField(null=True, default=None)
    AA15 = fields.TextField(null=True, default=None)
    AA16 = fields.TextField(null=True, default=None)
    AA17 = fields.TextField(null=True, default=None)
    AA18 = fields.TextField(null=True, default=None)
    AA19 = fields.TextField(null=True, default=None)
    AA20 = fields.TextField(null=True, default=None)
    AA21 = fields.TextField(null=True, default=None)
    AA22 = fields.TextField(null=True, default=None)
    AA23 = fields.TextField(null=True, default=None)
    AA24 = fields.TextField(null=True, default=None)

    #一对多
    # shou_utr = fields.ForeignKeyField("models.RiZhi",related_name="DaiShou")

    #多对多
    # duo = fields.ManyToManyField("models.RiZhi",related_name="DaiShou")



class DaiFu(Model):
    id = fields.IntField(description='id',pk=True)
    utr = fields.TextField(description='utr',default='')
    date_time = fields.TextField(description='date_time')
    card_id = fields.TextField(description='card_id')
    # fu_utr = fields.ForeignKeyField("models.RiZhi",related_name="DaiFu")



class RiZhi(Model):
    card_id = fields.TextField(description='编号')
    date_day = fields.TextField(description='日期')
    date_time = fields.TextField(description='上传时间')
    status = fields.TextField(description='状态')

