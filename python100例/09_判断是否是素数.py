'''
题目：判断101-200之间有多少个素数，并输出所有素数。
'''
import math
n = 0
for i in range(101,201):
    temp = 0
    for j in range(2,i):
        if i % j == 0:
            temp = 1
    if temp == 0:
        print(i)
        n+=1
print("总个数是：%d" % n)
