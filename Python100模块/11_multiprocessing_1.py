import time
from multiprocessing import Process
import os

def run(name):
    while True:
        time.sleep(2)
        print("子进程ID号:%d，run：%s" % (os.getpid(), name))  # os.getpid()进程ID

if __name__ == "__main__":
    print("父进程启动：%d" % os.getpid())
    # 创建子进程
    p = Process(target=run, args=("Ail",))  # target进程执行的任务, args传参数（元祖）
    p.start()   # 启动进程
    while True:
        print("死循环")
        time.sleep(1)
'''
由于Windows没有fork调用，而如果我们需要在Windows上用Python编写多进程的程序。
我们就需要使用到multiprocessing模块。
# 参数
multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})
- group：分组，实际上很少使用
- target：表示调用对象，你可以传入方法的名字
- name：别名，相当于给这个进程取一个名字
- args：表示被调用对象的位置参数元组，比如target是函数a，他有两个参数m，n，那么args就传入(m, n)即可
- kwargs：表示调用对象的字典
'''
