import multiprocessing

def worker(i):
    print("进程顺序是：%s" % i)
    name = multiprocessing.current_process().name
    print("进程名是：%s" % name)
    p = multiprocessing.current_process().ident
    print("pid是：%d " % p)
    print()

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker,args=(i,),name=("p%d " % i))
        jobs.append(p)
        p.start()
        p.join()   # 等待一个进程完成，在执行下一个进程（串行，没有并行效率高）
    print(jobs)
'''
p.daemon = True
类似于守护线程，守护进程会在主程序退出之前自动终止，以免留下孤儿进程。

p.terminate()
对一个进程对象调用terminate()会结束子进程。

p.exitcode
进程退出时生成的状态码可以通过exitcode属性访问
    ==0 未生成任何错误
    > 0 进程有一个错误，并以该错误码退出
    < 0 进程以一个-1*exitcode信号结束
'''
