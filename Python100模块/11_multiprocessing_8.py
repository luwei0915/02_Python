import multiprocessing
# 管理共享状态

def worker(d, key, value):
    mgr = multiprocessing.Manager()
    d[key] = value

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    d = mgr.dict()
    jobs = [
        multiprocessing.Process(
            target = worker,
            args = (d, i, i * 2),
        ) for i in range(10)
        ]
    for i in jobs:
        i.start()
    for j in jobs:
        j.join()
    print("D->", d)
