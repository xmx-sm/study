from flask import Flask, request
# from queue import Queue
from queue import Queue,LifoQueue,PriorityQueue
from threading import Thread
import time
from datetime import datetime

# app = Flask(__name__)
# queue = Queue()

# def process_queue():
#     while True:
#         if not queue.empty():
#             request = queue.get()
#             # 执行你的业务逻辑
#             # ...
#             queue.task_done()

# @app.route('/', methods=['POST'])
# def handle_request():
#     data = request.get_json()
#     # 将请求数据放入队列
#     queue.put(data)
#     return 'Request added to the queue.'

# if __name__ == '__main__':
#     # 启动队列处理线程
#     worker = Thread(target=process_queue)
#     worker.daemon = True
#     worker.start()
#     app.run()

def aa(name,de):
    pass
    # print(name)
    # time.sleep(10)
    # queue.get()
    # print('aaaaa',queue.queue)
def bb(name,de):
    # print(name)
    name = name +1
    print('queue.queue',name)
    print(queue.queue)
    print(datetime.now())
    print('-----------------------')
    time.sleep(30)
    # print('bbbbbb',queue.queue)
    aaa = queue.get()
    print('queue.get')
    print(aaa)
    print('-----------------------')
    
    queue.get()
    print('queue.queue',name)
    print(queue.queue)
    print(datetime.now())
    print('-----------------------')

bbb = 1
# 导入 Flask 模块
app = Flask(__name__)

# 创建一个队列对象2 
queue = Queue(maxsize=3)
# queue = Queue(maxsize=3)

# 定义一个函数来处理队列中的请求
def process_queue():
    global bbb
    # request = queue.get()z
    # print(queue.task_done())
    # print(queue.queue)
    bbb = bbb+1

    a = Thread(target=aa,args=(bbb, "猪猪"))
    b = Thread(target=bb,args=(bbb, "lalal"))
    a.start()
    b.start()


    # while True:
    #     if not queue.empty():
    #         request = queue.get()
    #         print(request)
    #         # 在这里执行你的业务逻辑
    #         # ...
    #         queue.task_done()

# 定义一个路由和对应的处理函数
@app.route('/', methods=['POST'])
def handle_request():
    # 从请求中获取 JSON 数据
    # data = request.get_json()
    data = request.form
    # 将请求数据放入队列
    queue.put(dict(data))
    process_queue()
    # print(queue.queue)
    return 'aaaaaa'

# 主程序入口
if __name__ == '__main__':
    # 启动一个新的线程来处理队列中的请求
    worker = Thread(target=process_queue)
    worker.daemon = True
    worker.start()
    # 运行 Flask 应用
    app.run()

