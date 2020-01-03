# 进程间的通信
import multiprocessing
import os

if __name__ == '__main__':
    print("进程启动：%d" % os.getpid())
    q = multiprocessing.Queue(3)
    q.put(1)
    q.put(2)
    q.put(3)

    print(q.full())             # 是否满了
    print(q.qsize())            # 输出大小

    print("-"*20)

    print(q.get())              # 先进先出 从队列读取并且删除一个元素。
    print(q.qsize())

    print("-"*20)

    print(q.empty())            # 是否为空
    print(q.qsize())
