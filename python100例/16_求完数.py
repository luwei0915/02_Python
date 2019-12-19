'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
因子：所有的因数
'''
for i in range(2,1000):
    l = []
    s = 0
    for j in range(1,i):
        if (i % j == 0):
            l.append(j)
    if l:                  # 不为空
        for k in l:
            s += k
        if (s == i):
            print(i)
            for m in l:
                print("%d " % m,end="")
            print()
