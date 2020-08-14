# Multithread execute method demo code.
# Ref : https://docs.python.org/3/library/threading.html
# Ref : https://www.tutorialspoint.com/python3/python_multithreading.htm
# Ref : https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/
import threading
import time
import random

def thread_demo():
    print(">> Basic thread demo")
    # 子執行緒的工作函數
    def job():
        for i in range(5):
            print("Child thread:", i)
            time.sleep(1)

    # 建立一個子執行緒
    t = threading.Thread(target = job)

    # 執行該子執行緒
    t.start()

    # 主執行緒繼續執行自己的工作
    for i in range(3):
        print("Main thread:", i)
        time.sleep(1)

    # 等待 t 這個子執行緒結束
    t.join()

    print("Done.")

def multithread_demo():
    print(">> Multithread demo")
    # 子執行緒的工作函數
    # 隨機休眠 1 ~ 2 秒後顯示參數代號
    def job(num):
        time.sleep(1 + 1*random.random())
        print("Thread", num)

    # 建立 5 個子執行緒
    threads = []
    for i in range(5):
        threads.append(threading.Thread(target = job, args = (i,)))
        threads[i].start()

    # 主執行緒繼續執行自己的工作
    # ...

    # 等待所有子執行緒結束
    for i in range(5):
        threads[i].join()

    print("Done.")

def multithread_class_demo():
    print(">> Multithread class demo")
    # 子執行緒類別
    class MyThread(threading.Thread):
        # Class constructor
        # Initial member variable by parameter.
        def __init__(self, num):
            threading.Thread.__init__(self)
            self.num = num

        # Thread execute function
        # Override function "run", ensure thread class start will execute it.
        def run(self):
            time.sleep(1 + 1*random.random())
            print("Thread", self.num)

    # 建立 5 個子執行緒
    threads = []
    for i in range(5):
        threads.append(MyThread(i))
        threads[i].start()

    # 主執行緒繼續執行自己的工作
    # ...

    # 等待所有子執行緒結束
    for i in range(5):
        threads[i].join()

    print("Done.")

thread_demo()
multithread_demo()
multithread_class_demo()
