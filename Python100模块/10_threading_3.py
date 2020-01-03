import threading, time
import random

def light():
    if not event.isSet():        #初始化evet的flag为真
        event.set()              #wait就不阻塞 绿灯状态
    count = 0
    while True:
        if count < 10:           # 0-9
            print('\033[42;1m---green light on---\033[0m')
        elif count < 13:         # 10-12
            print('\033[43;1m---yellow light on---\033[0m')
        elif count < 20:         # 12 -19
            if event.isSet():
                event.clear()    # 设置flag的值为假
            print('\033[41;1m---red light on---\033[0m')
        else:                     # >20,归0
            count = 0
            event.set()    # 打开绿灯
        time.sleep(1)
        count += 1

def car(n):
    while 1:
        time.sleep(random.randrange(3, 10))
        #print(event.isSet())
        if event.isSet():
            print("car [%s] is running..." % n)
        else:
            print('car [%s] is waiting for the red light...' % n)
            event.wait()    #红灯状态下调用wait方法阻塞，汽车等待状态

if __name__ == '__main__':
    car_list = ['BMW', 'AUDI', 'SANTANA']
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()                                          # light 线程开始
    for i in car_list:
        t = threading.Thread(target=car, args=(i,))        # 每种car一个线程
        t.start()
