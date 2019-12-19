'''
题目：一个5位数，判断它是不是回文数。
即12321是回文数，个位与万位相同，十位与千位相同。
'''
num = int(input("Input a number:"))
gewei = num % 10
wanwei = int(num / 10000)
shiwei = int(num % 100 / 10)
qianwei = int(num % 10000 / 1000)

if (gewei == wanwei) and (shiwei == qianwei):
    print("%d 是回文数" % num)
else:
    print("%d 不是回文数" % num)
