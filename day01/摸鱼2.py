import time
import threading
from queue import Queue
class CustomThread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.__queue=queue
    def run(self):
        while True:
            q_method=self.__queue.get()
            q_method()
            self.__queue.task_done()

def queue_pool():
    queue=Queue(6)
    for i in range(queue.maxsize):
        t = CustomThread(queue)
        t.setDaemon(True)
        t.start()
    for i in range(20):
        queue.put(moyu_time)
    queue.join()

def moyu_time(name,delay,counter):
        print("%s正在摸鱼%s"%(name,time.strftime("%Y-%m-%d &H:%M：%S",time.localtime()))
if __name__ == '__main__':
    queue_pool()