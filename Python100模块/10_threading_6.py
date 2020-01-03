import threading, time

def run(n):
    thread = threading.current_thread()
    thread.setName('Thread-***%s***' % n)
    print('-'*30)
    print("Pid is :%s" % thread.ident)  # 返回线程pid
    #print('ThreadName is :%s' % thread.name)  # 返回线程名称
    print('ThreadName is :%s'% threading.enumerate())    #返回所有线程对象列表
    time.sleep(2)

if __name__ == '__main__':
    #print('The current number of threads is: %s' % threading.active_count())
    threading.main_thread().setName('Chengd---python')
    for i in range(3):
        #print('The current number of threads is: %s' % threading.active_count())    #返回当前存活线程数量
        thread_alive = threading.Thread(target=run, args=(i,))
        thread_alive.start()
    thread_alive.join()
    print('\n%s thread is done...'% threading.current_thread().getName())
