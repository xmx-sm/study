from tortoise import Model
from tortoise import fields #字段
from typing import Union, Optional,List,Any, ClassVar
from pydantic import BaseModel, Field,field_validator,model_validator
from dataclasses import dataclass, field
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
class Fu_model(BaseModel):
    _custom_generated_pk: str = None  # 初始化为 None
    utr : Optional[str] = None
    date_time : Union[str, None] = None
    card_id : Union[str, None] = None
    # fields: List[Union[str, None]] = field(default_factory=lambda: [None] * 100)
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
    AA25 : Union[str, None] = None
    AA26 : Union[str, None] = None
    AA27 : Union[str, None] = None
    AA28 : Union[str, None] = None
    AA29 : Union[str, None] = None
    AA30 : Union[str, None] = None
    AA31 : Union[str, None] = None
    AA32 : Union[str, None] = None
    AA33 : Union[str, None] = None
    AA34 : Union[str, None] = None
    AA35 : Union[str, None] = None
    AA36 : Union[str, None] = None
    AA37 : Union[str, None] = None
    AA38 : Union[str, None] = None
    AA39 : Union[str, None] = None
    AA40 : Union[str, None] = None
    AA41 : Union[str, None] = None
    AA42 : Union[str, None] = None
    AA43 : Union[str, None] = None
    AA44 : Union[str, None] = None
    AA45 : Union[str, None] = None
    AA46 : Union[str, None] = None
    AA47 : Union[str, None] = None
    AA48 : Union[str, None] = None
    AA49 : Union[str, None] = None
    AA50 : Union[str, None] = None
    AA51 : Union[str, None] = None
    AA52 : Union[str, None] = None
    AA53 : Union[str, None] = None
    AA54 : Union[str, None] = None
    AA55 : Union[str, None] = None
    AA56 : Union[str, None] = None
    AA57 : Union[str, None] = None
    AA58 : Union[str, None] = None
    AA59 : Union[str, None] = None
    AA60 : Union[str, None] = None
    AA61 : Union[str, None] = None
    AA62 : Union[str, None] = None
    AA63 : Union[str, None] = None
    AA64 : Union[str, None] = None
    AA65 : Union[str, None] = None
    AA66 : Union[str, None] = None
    AA67 : Union[str, None] = None
    AA68 : Union[str, None] = None
    AA69 : Union[str, None] = None
    AA70 : Union[str, None] = None
    AA71 : Union[str, None] = None
    AA72 : Union[str, None] = None
    AA73 : Union[str, None] = None
    AA74 : Union[str, None] = None
    AA75 : Union[str, None] = None
    AA76 : Union[str, None] = None
    AA77 : Union[str, None] = None
    AA78 : Union[str, None] = None
    AA79 : Union[str, None] = None
    AA80 : Union[str, None] = None
    AA81 : Union[str, None] = None
    AA82 : Union[str, None] = None
    AA83 : Union[str, None] = None
    AA84 : Union[str, None] = None
    AA85 : Union[str, None] = None
    AA86 : Union[str, None] = None
    AA87 : Union[str, None] = None
    AA88 : Union[str, None] = None
    AA89 : Union[str, None] = None
    AA90 : Union[str, None] = None
    AA91 : Union[str, None] = None
    AA92 : Union[str, None] = None
    AA93 : Union[str, None] = None
    AA94 : Union[str, None] = None
    AA95 : Union[str, None] = None
    AA96 : Union[str, None] = None
    AA97 : Union[str, None] = None
    AA98 : Union[str, None] = None
    AA99 : Union[str, None] = None
    AA100 : Union[str, None] = None
    fields_to_convert: ClassVar[List[str]] = ['utr', 'date_time', 'card_id','AA1','AA2','AA3','AA4','AA5','AA6','AA7','AA8','AA9','AA10','AA11','AA12','AA13','AA14','AA15','AA16','AA17','AA18','AA19','AA20','AA21','AA22','AA23','AA24','AA25','AA26','AA27','AA28','AA29','AA30','AA31','AA32','AA33','AA34','AA35','AA36','AA37','AA38','AA39','AA40','AA41','AA42','AA43','AA44','AA45','AA46','AA47','AA48','AA49','AA50','AA51','AA52','AA53','AA54','AA55','AA56','AA57','AA58','AA59','AA60','AA61','AA62','AA63','AA64','AA65','AA66','AA67','AA68','AA69','AA70','AA71','AA72','AA73','AA74','AA75','AA76','AA77','AA78','AA79','AA80','AA81','AA82','AA83','AA84','AA85','AA86','AA87','AA88','AA89','AA90','AA91','AA92','AA93','AA94','AA95','AA96','AA97','AA98','AA99','AA100']
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
        print('.........................................')
        df = pd.read_excel(str(file_path) + '/' + str(file_name))
        old_name = df.columns.to_list()
        new_name = {}
        for i in range(len(old_name)):
            new_name[old_name[i]] = "AA"+str(i)
        df.rename(columns=new_name,inplace=True)
        df.to_excel(str(file_path) + '/' + str(file_name),index=False)
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
    AA25 = fields.TextField(null=True, default=None)
    AA26 = fields.TextField(null=True, default=None)
    AA27 = fields.TextField(null=True, default=None)
    AA28 = fields.TextField(null=True, default=None)
    AA29 = fields.TextField(null=True, default=None)
    AA30 = fields.TextField(null=True, default=None)
    AA31 = fields.TextField(null=True, default=None)
    AA32 = fields.TextField(null=True, default=None)
    AA33 = fields.TextField(null=True, default=None)
    AA34 = fields.TextField(null=True, default=None)
    AA35 = fields.TextField(null=True, default=None)
    AA36 = fields.TextField(null=True, default=None)
    AA37 = fields.TextField(null=True, default=None)
    AA38 = fields.TextField(null=True, default=None)
    AA39 = fields.TextField(null=True, default=None)
    AA40 = fields.TextField(null=True, default=None)
    AA41 = fields.TextField(null=True, default=None)
    AA42 = fields.TextField(null=True, default=None)
    AA43 = fields.TextField(null=True, default=None)
    AA44 = fields.TextField(null=True, default=None)
    AA45 = fields.TextField(null=True, default=None)
    AA46 = fields.TextField(null=True, default=None)
    AA47 = fields.TextField(null=True, default=None)
    AA48 = fields.TextField(null=True, default=None)
    AA49 = fields.TextField(null=True, default=None)
    AA50 = fields.TextField(null=True, default=None)
    AA51 = fields.TextField(null=True, default=None)
    AA52 = fields.TextField(null=True, default=None)
    AA53 = fields.TextField(null=True, default=None)
    AA54 = fields.TextField(null=True, default=None)
    AA55 = fields.TextField(null=True, default=None)
    AA56 = fields.TextField(null=True, default=None)
    AA57 = fields.TextField(null=True, default=None)
    AA58 = fields.TextField(null=True, default=None)
    AA59 = fields.TextField(null=True, default=None)
    AA60 = fields.TextField(null=True, default=None)
    AA61 = fields.TextField(null=True, default=None)
    AA62 = fields.TextField(null=True, default=None)
    AA63 = fields.TextField(null=True, default=None)
    AA64 = fields.TextField(null=True, default=None)
    AA65 = fields.TextField(null=True, default=None)
    AA66 = fields.TextField(null=True, default=None)
    AA67 = fields.TextField(null=True, default=None)
    AA68 = fields.TextField(null=True, default=None)
    AA69 = fields.TextField(null=True, default=None)
    AA70 = fields.TextField(null=True, default=None)
    AA71 = fields.TextField(null=True, default=None)
    AA72 = fields.TextField(null=True, default=None)
    AA73 = fields.TextField(null=True, default=None)
    AA74 = fields.TextField(null=True, default=None)
    AA75 = fields.TextField(null=True, default=None)
    AA76 = fields.TextField(null=True, default=None)
    AA77 = fields.TextField(null=True, default=None)
    AA78 = fields.TextField(null=True, default=None)
    AA79 = fields.TextField(null=True, default=None)
    AA80 = fields.TextField(null=True, default=None)
    AA81 = fields.TextField(null=True, default=None)
    AA82 = fields.TextField(null=True, default=None)
    AA83 = fields.TextField(null=True, default=None)
    AA84 = fields.TextField(null=True, default=None)
    AA85 = fields.TextField(null=True, default=None)
    AA86 = fields.TextField(null=True, default=None)
    AA87 = fields.TextField(null=True, default=None)
    AA88 = fields.TextField(null=True, default=None)
    AA89 = fields.TextField(null=True, default=None)
    AA90 = fields.TextField(null=True, default=None)
    AA91 = fields.TextField(null=True, default=None)
    AA92 = fields.TextField(null=True, default=None)
    AA93 = fields.TextField(null=True, default=None)
    AA94 = fields.TextField(null=True, default=None)
    AA95 = fields.TextField(null=True, default=None)
    AA96 = fields.TextField(null=True, default=None)
    AA97 = fields.TextField(null=True, default=None)
    AA98 = fields.TextField(null=True, default=None)
    AA99 = fields.TextField(null=True, default=None)
    AA100 = fields.TextField(null=True, default=None)



class RiZhi(Model):
    # id = fields.IntEnumField((time.time)*1000,pk = True)
    card_id = fields.TextField(description='编号')
    date_day = fields.TextField(description='日期')
    date_time = fields.TextField(description='上传时间')
    status = fields.TextField(description='状态')

if __name__ == '__main__':
    print(datetime.now())