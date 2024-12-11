'''
os.fork()
multiprocessing
subprocess
'''

# 方式1
from multiprocessing import Process
import time


# def func(name):
#     print(f'{name}任务开始')
#     time.sleep(5)
#     print(f'{name}任务执行完毕')


# if __name__ == '__main__':
#     # 1、得到进程操作对象
#     p = Process(target=func, args=('写讲话稿',))
#     # 2、创建进程
#     p.start()
#     print('主进程')


# 方式2
from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.task_name = name

    def run(self):
        print(f'{self.task_name}任务开始')
        time.sleep(5)
        print(f'{self.task_name}任务结束')


if __name__ == '__main__':
    p = MyProcess('1')
    print('主进程1')
    p.start()
    p = MyProcess('2')
    print('主进程2')
    p.start()
    print('主进程3')
