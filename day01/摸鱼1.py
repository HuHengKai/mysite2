import time
import threading
class MyThread(threading.Thread):
    def __init__(self,threadID,name,count):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.count=count
    def run(self):
        print("开始线程"+self.name)
        moyu_time(self.name,self.count,10)
        print("推出线程"+self.name)

def moyu_time(threadName,delay,count):
    while count:
        time.sleep(delay)
        print("%s开始摸鱼%s"%(threadName,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        count=count-1
thread1=MyThread(1,"小明",1)
thread2=MyThread(2,"小红",2)
thread5 = MyThread(55, "小青", 2)
thread6 = MyThread(56, "小白", 2)
thread7 = MyThread(57, "小狗", 2)

thread1.start()
thread2.start()

thread5.start()
thread6.start()

thread7.start()

thread1.join()
thread2.join()
thread5.join()
thread6.join()
thread7.join()

print("退出主线程")
# if __name__=='__main__':
#     moyu_time('小帅',1,20)