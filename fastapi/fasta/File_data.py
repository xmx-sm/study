import pandas as pd
import os,json
from models import shou

import uvicorn
from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM
# from api.student import student_api

app = FastAPI()

def xlsx_revise(file_path):
    print(file_path)
    df = pd.read_excel(file_path)
    old_name = df.columns.to_list()
    new_name = {}
    for i in range(len(old_name)):
        new_name[old_name[i]] = "AA"+str(i)
    df.rename(columns=new_name,inplace=True)
    df.to_excel(file_path,index=False)


class file_data():
    def __init__(self,file_path):
        self.file_path = file_path
        file_list = os.listdir(file_path)
        for file_name in file_list:
            file_name_sp = file_name.split('.')
            if file_name_sp[-1] == 'xlsx':
                file_path = os.path.join(self.file_path + '/' + file_name)
                xlsx_revise(file_path)
            else:
                print(file_name_sp)




if __name__ == '__main__':
    register_tortoise(
        app=app,
        config=TORTOISE_ORM,
    )