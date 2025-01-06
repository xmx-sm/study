from tortoise import Model
from tortoise import fields #字段
from typing import Union, Optional,List,Any, ClassVar
from pydantic import BaseModel, Field,field_validator,model_validator
import pandas as pd,json,os
from datetime import datetime
import uuid,time

class Shou_model(BaseModel):
    _custom_generated_pk: str = None  # 初始化为 None
    utr : Optional[str] = None
    date_time : Union[str, None] = None
    card_id : Union[str, None] = None
    AA1 : Union[str, None] = None
    AA2 : Union[str, None] = None
    AA3 : Union[str, None] = None
    AA4 : Union[str, None] = None
    AA5 : Union[str, None] = None
    AA6 : Union[str, None] = None
    AA7 : Union[str, None] = None
    AA8 : Union[str, None] = None
    AA9 : Union[str, None] = None
    AA10 : Union[str, None] = None
    AA11 : Union[str, None] = None
    AA12 : Union[str, None] = None
    AA13 : Union[str, None] = None
    AA14 : Union[str, None] = None
    AA15 : Union[str, None] = None
    AA16 : Union[str, None] = None
    AA17 : Union[str, None] = None
    AA18 : Union[str, None] = None
    AA19 : Union[str, None] = None
    AA20 : Union[str, None] = None
    AA21 : Union[str, None] = None
    AA22 : Union[str, None] = None
    AA23 : Union[str, None] = None
    AA24 : Union[str, None] = None

    fields_to_convert: ClassVar[List[str]] = ['utr', 'date_time', 'card_id','AA1','AA2','AA3','AA4','AA5','AA6','AA7','AA8','AA9','AA10','AA11','AA12','AA13','AA14','AA15','AA16','AA17','AA18','AA19','AA20','AA21','AA22','AA23','AA24']
    # @model_validator(mode='before')
    # def generate_custom_pk(cls, values: dict) -> dict:
    #     if '_custom_generated_pk' not in values:
    #         values['_custom_generated_pk'] = str(uuid.uuid4())  # 生成 UUID 作为自定义主键
    #     return values
    @field_validator(*fields_to_convert, mode='before')
    def convert_to_string(cls, v: Any) -> str:
        if v is not None:
            return str(v)
        return ""

class excel_data():
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
        os.remove(str(file_path) + '/' + str(file_name))
    def xls_revise(file_path,file_name):
        df = pd.read_excel(str(file_path) + '/' + str(file_name), engine='xlrd')
        old_name = df.columns.to_list()
        new_name = {}
        for i in range(len(old_name)):
            new_name[old_name[i]] = "AA"+str(i)
        df.rename(columns=new_name,inplace=True)
        file_new_name = str(file_name).split('.')[0] + '.xlsx'
        df.to_excel(str(file_path) + '/' + str(file_new_name),index=False)
        os.remove(str(file_path) + '/' + str(file_name))
    def excel_read_data(file_path,file_name):
        df = pd.read_excel(str(file_path) + '/' + str(file_name))
        data = df.to_json(orient='records')
        data_json = json.loads(data)
        file_name_sp = str(file_name).split('.')[0]
        file_new_name = file_name_sp.split('-')
        # print(len(data_json))
        if file_new_name[0] == 'BOM':
            datetime_time = datetime.now()
            for i in range(len(data_json)):
                # print(data_json[i])
                data_json[i]['utr'] = data_json[i]["AA3"]
                data_json[i]['date_time'] = datetime_time
                data_json[i]['card_id'] = str(file_new_name[0])+str(file_new_name[1])

        elif file_new_name[0] == 'IOB':
            datetime_time = datetime.now()
            for i in range(len(data_json)):
                data_json[i]['utr'] = data_json[i]["AA3"]
                data_json[i]['date_time'] = datetime_time
                data_json[i]['card_id'] = str(file_new_name[0])+str(file_new_name[1])
        else:
            for i in range(len(data_json)):
                data_json[i]['card_id'] = str(file_new_name[0])+str(file_new_name[1])

        return data_json,file_new_name[2]


class DaiShou(Model):
    # id = fields.IntField(pk = True)
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
    # id = fields.IntEnumField((time.time)*1000,pk = True)
    id = fields.IntField(description='id',pk=True)
    utr = fields.TextField(description='utr',default='')
    date_time = fields.TextField(description='date_time')
    card_id = fields.TextField(description='card_id')
    # fu_utr = fields.ForeignKeyField("models.RiZhi",related_name="DaiFu")



class RiZhi(Model):
    # id = fields.IntEnumField((time.time)*1000,pk = True)
    card_id = fields.TextField(description='编号')
    date_day = fields.TextField(description='日期')
    date_time = fields.TextField(description='上传时间')
    status = fields.TextField(description='状态')

if __name__ == '__main__':
    print(datetime.now())