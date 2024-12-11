'''
时间：2021.8.11
作者：手可摘星辰不去高声语
名称：02-使用多进程实现多任务.py
'''
 
# 1.导入包和模块
import multiprocessing
import time
 
 
def sing():
    for i in range(3):
        print("i am sing ooo~")
        time.sleep(0.5)
 
 
def dance():
    for i in range(3):
        print("i am dance lll~")
        time.sleep(0.5)
 
 
if __name__ == '__main__':
    # 2.使用进程类创建进程对象
    # target ：指定进程执行的函数名，不加括号
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)
 
    # 3. 使用进程对象启动进程执行指定任务
    sing_process.start()
    dance_process.start()