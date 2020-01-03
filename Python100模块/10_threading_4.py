import threading, time

# threading.active_count()

def run():
    thread = threading.current_thread()
    print('%s is running...'% thread.getName())    #返回线程名称
    time.sleep(10)    #休眠10S方便统计存活线程数量

if __name__ == '__main__':
    for i in range(10):
        print('The current number of threads is: %s' % threading.active_count())
        thread_alive = threading.Thread(target=run, name='Thread-***%s***' % i)
        thread_alive.start()                   # 开启10个线程
    thread_alive.join()
    print('\n%s thread is done...'% threading.current_thread().getName())
