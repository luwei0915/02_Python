'''
题目：求100之内的素数。
'''
for i in range(2,101):
    temp = 0
    for j in range(2,i):
        if (i % j == 0):
            temp = 1
    if (temp == 0):
        print(i)
