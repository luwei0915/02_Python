import threading, time

# 模拟捉迷藏游戏
def Seeker(cond, name):
    time.sleep(2)
    cond.acquire()                               # 加锁
    print('%s :我已经把眼睛蒙上了！'% name)
    cond.notify()                                # 通知_我蒙上眼睛
    cond.wait()                                  # 等待_是否藏好
    for i in range(3):
        print('%s is finding!!!'% name)
        time.sleep(2)
    cond.notify()                                # 通知_寻找者正在寻找
    cond.release()                               # 解锁
    print('%s :我赢了！'% name)

def Hider(cond, name):
    cond.acquire()                               # 加锁
    cond.wait()                                  # 等待_是否眼睛蒙好
    for i in range(2):
        print('%s is hiding!!!'% name)
        time.sleep(3)
    print('%s :我已经藏好了，你快来找我吧！'% name)
    cond.notify()                                # 通知_我已经藏好了
    cond.wait()                                  # 等待，被找到
    cond.release()                               # 解锁，被找到
    print('%s :被你找到了，唉~^~!'% name)

if __name__ == '__main__':
    cond = threading.Condition()
    seeker = threading.Thread(target=Seeker, args=(cond, 'seeker'))
    hider = threading.Thread(target=Hider, args=(cond, 'hider'))
    seeker.start()
    hider.start()
'''
流程分析：seeker与hider为两个独立线程
01 seeker加锁，notify其我蒙上眼睛，并wait
02 hider加锁，wait
03 hider接收到seeker的notify,知道其蒙上眼睛，发出hiding消息
04 hide notify 藏好了消息，并wait
05 seeker的wait收到hider的notify，发出finding消息
06 seeker notify找到了消息，解锁
07 hider的wait收到seeker的找到了消息，发出认输的消息，解锁
'''
