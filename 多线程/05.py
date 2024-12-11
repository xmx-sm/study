import threading
import time

# 为线程定义一个函数
class myThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
    def run(self):
        # print("Starting " + self.name)
        # print_time(self.name, self.delay)
        # print("Exiting " + self.name)
        time.sleep(3)
        print(self.delay)
        
# def print_time(threadNmae, delay):
#     counter = 0
#     while counter < 3:
#         time.sleep(delay)
#         print(threadNmae, time.ctime())
#         counter += 1
        
threads = []

# 创建新线程
thread1 = myThread(name="Thread-1", delay=1)
thread2 = myThread(name="Thread-2", delay=2)
thread3 = myThread(name="Thread-3", delay=3)

# 开启新线程
thread1.start()
thread2.start()
thread3.start()

# 添加新线程到线程列表
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

print('aaaaa:',threading.active_count())
print('bbbbbb:',threads)

# 等待所有线程完成
for t in threads:
    t.join()
    
print("线程结束")
