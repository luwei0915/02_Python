# 生产者-消费者模型
from multiprocessing import Process, JoinableQueue
import time,random

def consumer(q,name):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('%s 吃 %s' % (name, res))
        q.task_done() # 发送信号给q.join()，说明已经从队列中取走一个数据并处理完毕了

def producer(q, name, food):
     for i in range(3):
         time.sleep(random.randint(1, 3))
         res = '%s%s' % (food, i)
         q.put(res)
         print('%s 生产了 %s' % (name, res))
         q.join()  # 等到消费者把自己放入队列中的所有的数据都取走之后，生产者才结束

if __name__ == '__main__':
    q = JoinableQueue()  # 使用JoinableQueue()
    # 生产者们
    p1 = Process(target=producer, args=(q, 'egon1', '包子'))
    p2 = Process(target=producer, args=(q, 'egon2', '骨头'))
    p3 = Process(target=producer, args=(q, 'egon3', '泔水'))
    # 消费者们
    c1 = Process(target=consumer, args=(q, 'alex1'))
    c2 = Process(target=consumer, args=(q, 'alex2'))
    c1.daemon = True
    c2.daemon = True
    # 开始
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()

    print('主process')
#1、主进程等生产者p1、p2、p3结束
#2、而p1、p2、p3是在消费者把所有数据都取干净之后才会结束
#3、所以一旦p1、p2、p3结束了，证明消费者也没必要存在了，应该随着主进程一块死掉，
#   因而需要将消费者们设置成守护进程
