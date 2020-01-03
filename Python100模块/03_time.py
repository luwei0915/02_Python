import time
s = time.time()
# 1576805999.8585556   时间戳

s = time.ctime()
# Fri Dec 20 09:40:39 2019

s = time.ctime(time.time() + 600)
# Fri Dec 20 09:51:54 2019

# time.sleep(3)  暂停三秒

# s = time.clock()
# 0.1931411      程序实际运行时间

s = time.gmtime()
# time.struct_time(tm_year=2019, tm_mon=12, ,,,

s = time.gmtime().tm_mon
# 12 月份

s = time.gmtime().tm_yday
# 354

s = time.localtime()
# time.struct_time(tm_year=2019, tm_mon=12, tm_mday=20,
# tm_hour=9, tm_min=51, tm_sec=40, tm_wday=4, tm_yday=354, tm_isdst=0)

s = time.strftime(time.ctime())
# Fri Dec 20 10:08:25 2019

s = time.strftime('%Y-%m-%d')
# 2019-12-20

s = time.strftime('%Y-%m-%d %H:%M:%S')
# 2019-12-20 10:10:45
