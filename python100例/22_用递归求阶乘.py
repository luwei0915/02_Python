'''
题目：利用递归方法输出：
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
'''
def fact(n):
    sum = 0
    if n == 0:
        sum = 1
    else:
        sum = n*fact(n-1)
    return sum
for i in range(6):
    print("%d! = %d" % (i,fact(i)))
