import time

t1 = time.time()
print(t1)

time.sleep(1)

t2 = time.localtime(t1)
print(t2)

time.sleep(1)

t3 = time.strftime('%Y-%m-%d %H:%M:%S',t2)
print(t3)
