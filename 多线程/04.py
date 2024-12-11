'''
时间：2021.8.11
作者：手可摘星辰不去高声语
名称：07-进程注意点-设置守护主进程.py
'''
 
# 1.导入包和模块
import multiprocessing
import time
 
 
def work():
    # 子进程工作2秒
    for i in range(10):
        print("工作中…")
        time.sleep(3)
 
 
if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    # 设置守护主进程，主进程退出后子进程直接销毁，不再执行子进程的代码
    work_process.daemon = True
    work_process.start()
    
 
    # 主进程睡眠1秒
    time.sleep(4)
    print("主进程执行完……")