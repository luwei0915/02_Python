'''
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
'''

def pf(x):
    return x*x

Right = 1
Wrong = 0
again = 1
while again:
    n = int(input("Num:"))
    s = pf(n)
    print("The result is %d\n" % s)
    if ( s < 50 ):
        again = Right
    else:
        again = Wrong
