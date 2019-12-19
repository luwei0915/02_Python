'''
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
'''
num = int(input("Row:"))                 # 控制输出的行数

a = []
b = []
c = []
len_a = len(a)
len_c = len(c)

for i in range(1,num+1):
    if ( i< 3 ):
        while len_a < i:
            a.append(1)
            len_a = len(a)
        print(a)
        c = a.copy()                     # 构造出 [ 1, 1 ] ,每次在此插入数据
        b = a.copy()
    else:
        len_c = len(c)
        j = 1
        while len_c < i:
            c.insert(j,b[j-1] + b[j])
            j += 1
            len_c = len(c)               # 判断长度，终止循环
        print(c)
        b = c.copy()
        c = a.copy()
