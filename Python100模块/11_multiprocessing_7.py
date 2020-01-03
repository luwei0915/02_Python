# 控制资源的访问
import multiprocessing
import time

def stage_1(cond):
    name = multiprocessing.current_process().name
    print("starting", name)
    with cond:
        print("{} done and ready for stage 2".format(name))
        # 激活等待的进程
        cond.notify_all()

def stage_2(cond):
    name = multiprocessing.current_process().name
    print("starting", name)
    with cond:
        cond.wait()
        print("{} running".format(name))

if __name__ == '__main__':
    condition = multiprocessing.Condition()
    s1 = multiprocessing.Process(name="s1",target=stage_1,args=(condition, ),)
    s2_client = [
        multiprocessing.Process(
            name="stage_2[{}]".format(i),
            target=stage_2,
            args=(condition, ),
        ) for i in range(1, 3)]
    for c in s2_client:
        c.start()
        time.sleep(1)
    s1.start()
    s1.join()
    for c in s2_client:
        c.join()

'''
如果需要在多个进程间共享一个资源，可以使用一个Lock锁来避免访问冲突。
lock = multiprocessing.Lock() 实例化一个锁对象
lock.acquire() 加锁
lock.release() 释放锁
with lock： # 拿到锁执行代码后并释放锁，注意不要嵌套

控制资源的并发访问
有时候允许多个进程同时访问一个资源，但是要限制总数。
比如一个网络应用可能支持固定数目的并发下载。用Semaphore来管理这些连接.
3是允许同时访问的最大进程数。
s = multiprocess.Semaphore(3)
obs = [
    multiprocess.Process(
    target=worker,
    name=str(i),
    args=(s,)) for i in range(10)]
    ...
'''
