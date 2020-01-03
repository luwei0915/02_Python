import threading,time
s = 0
lock = threading.Lock()
rlk = threading.RLock()

print("---------threading.Lock()-----------")
def change_it(n):
    global s
    s += n
    s -= n

def run_thread(n):
    for i in range(10000):
        lock.acquire()          # 上锁
        try:
            change_it(n)
        finally:
            lock.release()      # 释放锁

# d多个线程操作s的值，没有线程锁的话，可能造成混乱
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(s)

print("--------threading.Rlock()----------")
# RLock允许在同一线程中被多次acquire,与release成对出现
rlk.acquire()
rlk.acquire()
rlk.release()
rlk.release()

print("--------threading.Condition()----------")


'''
threading.currentThread()
返回当前的线程变量

threading.enumerate()
返回一个包含正在运行的线程的list。
正在运行指线程启动后、结束前，不包括启动前和终止后的线程。

threading.activeCount()
返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

run()
用以表示线程活动的方法

start()
启动线程活动

join([time])
等待至线程中止。这阻塞调用线程直至线程的join()

isAlive()
返回线程是否活动的。

getName()
返回线程名

setName()
设置线程名。

线程锁
threading.Lock()
threading.RLock()
threading.Condition()
     wait([timeout]):线程挂起，直到收到一个notify通知或者超时
                    （可选的，浮点数，单位是秒s）才会被唤醒继续运行。
     notify(n=1):通知其他线程，那些挂起的线程接到这个通知之后会开始运行，
                  默认是通知一个正等待该condition的线程,最多则唤醒n个等待的线程。
     notifyAll(): 如果wait状态线程比较多，notifyAll的作用就是通知所有线程
threading.Event 事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，
                那么当程序执行 event.wait 方法时就会阻塞；如果“Flag”值为True，
                那么执行event.wait 方法时便不再阻塞。
                clear：将“Flag”设置为False
                set：将“Flag”设置为True
threading.get_ident()     返回线程pid
threading.main_thread()   返回主线程对象，类似 threading.current_thread()

'''
