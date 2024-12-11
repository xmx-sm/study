'''
时间：2021.8.11
作者：手可摘星辰不去高声语
名称：06-进程注意点.py
'''
 
# 1.导入包和模块
import multiprocessing
import time
 
 
def work():
    # 子进程工作2秒
    for i in range(10):
        print("工作中…")
        time.sleep(0.2)
 
 
if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    work_process.start()
 
    # 主进程睡眠1秒
    # time.sleep(5)
    print("主进程执行完……")
