# 派生进程
import multiprocessing
import os

class Worker(multiprocessing.Process):
    print("子进程启动：%d" % os.getpid())
    def run(self):
        print("In{}\n".format(self.name))
        return
if __name__ == '__main__':
    print("父进程启动：%d" % os.getpid())
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()                               # 此处跳到类的方法中执行，之后进行下一步
        p.join()
        print(p.is_alive())
    print("父进程依然存在：%d" % os.getpid())
    # for j in jobs:
    #     j.join()
    # print(p.is_alive())
