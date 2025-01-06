# from enum import IntEnum
# from tortoise import models
# from tortoise import fields



# class AbstractModel(models.Model):
#     # 主键，当表里所有属性都没设置pk时，默认生成一个IntField类型 id 的主键
#     id = fields.UUIDField(pk=True)

#     class Meta:
#         # 抽象模型，不生成表
#         abstract = True


# class MixinTimeFiled:
#     # 添加数据时间
#     created = fields.DatetimeField(null=True, auto_now_add=True)
#     # 修改数据时间
#     modified = fields.DatetimeField(null=True, auto_now=True)


# class Gender(IntEnum):
#     MAN = 0
#     WOMAN = 1


# class UserModel(AbstractModel, MixinTimeFiled):
#     # unique 是否唯一 max—length 数据长度 index 是否索引
#     username = fields.CharField(max_length=20, description="描述", unique=True, index=True)
#     # null 是否可以为空
#     nickname = fields.CharField(max_length=30, description='nickname', null=True, default='777')
#     # description 字段备注 ddl展示， 此处入库的为 0 or 1
#     gender = fields.IntEnumField(Gender, description='sex', default=Gender.WOMAN)
#     # max——digits 小输点左边最大位数，decimal——places 小数点右边最大位数
#     balance = fields.DecimalField(max_digits=2, decimal_places=2, description='balance')
#     is_admin = fields.BooleanField(default=False)
#     job_info = fields.JSONField(default=dict)

#     class Meta:
#         # 自定义表名，不配置按照类名小写生成
#         table = "tableName"
#         table_description = "set table ddl desc"

#         # # 多列设置唯一复合所有
#         # unique_together = (('gender', 'balance'),)
#         # # 排序
#         # ordering = ('is_admin',)
#         # # 索引
#         # indexes = ('balance',)


# # async def init():
# #     # Here we create a SQLite DB using file "db.sqlite3"
# #     #  also specify the app name of "models"
# #     #  which contain models from "app.models"
# #     await Tortoise.init(
# #         # 数据库连接
# #         # db_url='sqlite://db.sqlite3',
# #         # 连接mysql pip install aiomysql
# #         db_url='mysql://root:000117@127.0.0.1:3306/cckj',
# #         # 指定管理的models，__main__ 🈯️当前文件的models.Model
# #         modules={'models': ['__main__']}
# #     )
# #     # Generate the schema
# #     await Tortoise.generate_schemas()

# # if __name__ == '__main__':
# #     run_async(init())

# from Sqllog import TORTOISE_ORM
# from tortoise import Model, fields, Tortoise, run_async

# class shou():
#     def chuangjian():
#         class set(Model):
#             id = fields.IntField(pk=True)
#             name = fields.CharField(max_length=255)
#             class Meta:
#                 table = "set"

# if  __name__ == '__main__':
#     run_async(shou.chuangjian())

from tortoise import Model
from tortoise import fields #字段

# from settings import TORTOISE_ORM



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

