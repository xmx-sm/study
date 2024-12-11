import threading
import time

VALUE = 0
gLock = threading.Lock()

def xc_a():
    global VALUE
    gLock.acquire()
    for i in range(0,5):
        print('xc_a',i)
        time.sleep(1)
        # gLock.release()
        if i == 2:
           threading.Condition().notify_all()
    print('xc_a77',threading.current_thread())

def xc_b():
    global VALUE
    gLock.acquire()
    for i in range(0,5):
        print('xc_b',i)
        time.sleep(3)

    gLock.release()
    print('xc_b111',threading.enumerate())


def multi_thread():
  t1 = threading.Thread(target=xc_a)
  t2 = threading.Thread(target=xc_b)

  t1.start()
  t2.start()
#   for x in range(0,3):
#     t = threading.Thread(target=xc_a)
#     t.start()
#     print('第次',x)


if __name__ == '__main__':
  multi_thread()

# import threading
# import time

# VALUE = 0

# gLock = threading.Lock()

# def add_value():
#   global VALUE
#   gLock.acquire()
#   for x in range(5):
#     VALUE += 1
#     print(x)
#     time.sleep(3)
    
#   gLock.release()
# #   print('value：%d'%VALUE)
#   print('aa',x)

# def main():
#   for x in range(1):
#     t = threading.Thread(target=add_value)
#     t.start()
#     print('main11',x)
#     time.sleep(7)


# if __name__ == '__main__':
#   main()
