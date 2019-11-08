import os
L12 = [d for d in os.listdir('.')]  # 列出当前文件和目录，以逗号分隔
print(L12)

L=[]
n=1
while n <= 9:
    L.append(n)
    n+=2
print(L)

L1 = ['a','b','c','d']  # 切片
L2 = []
for i in range(2):
    L2.append(L1[i])
print(L2)
L3 = L1[:3]
L4 =L1[-2:]
L5 = L1[1:2]
print(L3,L4,L5)

L6 = list(range(6))
L7 = L6[:5:2]  # 步长
print(L6,L7)

L8='abcdefg'[:5:2]  # 字符串切片
print(L8)

L9 = list(range(2,10))
print(L9)

L10 = [x * x for x in range(1,5) ]  # 列表生成式
print(L10)
L11 = [m + n for m in 'abc' for n in 'xyz']
print(L11)

d1 = {'a':'A','b':'B','c':'C','d':'D'}
for  k,v in d1.items():
    print(k,'=',v)
L13 = [m + '=' + n for m,n in d1.items()]
print(L13)

L14 = ['HELLO','HAHA']
L15 = [s.lower() for s in L14]
print(L15)
