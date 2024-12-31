from pydantic import BaseModel, EmailStr
# from typing import Union,Optional
from tortoise import fields, Model

class Utr(BaseModel):
    utr: str = None

class Shou(Model):

    A08 = fields.CharField(max_length=50, pk=True)
    A01 = fields.CharField(max_length=500)
    class Meta:
        table = "shou"

# class Fu(Model):
#     id = fields.IntField(description="A08")

# class Student(Model):
#     id = fields.IntField(pk=True)
#     name = fields.CharField(max_length=32, description="姓名")
#     pwd = fields.CharField(max_length=32, description="密码")
#     sno = fields.IntField(description="学号")

#     # 一对多的关系
#     clas = fields.ForeignKeyField("models.Clas", related_name="students")

#     # 多对多的关系
#     courses = fields.ManyToManyField("models.Course", related_name="students")


# class Course(Model):
#     id = fields.IntField(pk=True)
#     name = fields.CharField(max_length=32, description="课程名称")
#     teacher = fields.ForeignKeyField("models.Teacher", )
#     # addr = fields.CharField(max_length=32, description="教室", default="")


# class Clas(Model):
#     id = fields.IntField(pk=True)
#     name = fields.CharField(max_length=32, description="班级名称")


# class Teacher(Model):
#     id = fields.IntField(pk=True)
#     name = fields.CharField(max_length=32, description="姓名")
#     pwd = fields.CharField(max_length=32, description="密码")
#     tno = fields.IntField(description="老师编号")
