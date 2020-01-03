import datetime

# 获取格式化的日期
n = datetime.date.today()
# 2019-12-20

# 获取自定义格式化的日期
n1 = n.strftime("%Y %m %d")
# 2019 12 20

#设置日期
n2 = datetime.date(2000,10,10)
# 2000-10-10

#日期算数运算
n3 = n2 + datetime.timedelta(days=-10)
# 2000-09-30

# 日期替换
n4 = n2.replace(year=n2.year+1000)
# 3000-10-10
