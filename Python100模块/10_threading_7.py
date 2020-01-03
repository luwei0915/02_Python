import threading, time

def run(n):
    print('-'*30)
    print("Now Pid is :%s" % threading.current_thread().ident)           # 返回当前线程pid
    print("Main Pid is :%s" % threading.main_thread().ident)             # 返回主线程pid
    print('Now thread is %s...' % threading.current_thread().getName())  # 获取当前线程名
    print('Main thread is %s...' % threading.main_thread().getName())    # 获取主线程线程名

if __name__ == '__main__':
    threading.main_thread().setName('Chengd---python')                   # 自定义线程名
    for i in range(3):
        thread_alive = threading.Thread(target=run, args=(i,))
        thread_alive.start()
        time.sleep(2)
    thread_alive.join()
