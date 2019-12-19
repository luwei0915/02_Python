'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
'''
times = int(input("次数："))
num = int(input("数字："))
j = 1
s = 0
for i in range(times):
    s += num * j*10**i
    if (i != times - 1):
       print("%d + " % s,end="")
    else:
        print("%d" % s, end="")
