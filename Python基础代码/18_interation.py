from collections import Iterable  # 判断是否可迭代
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))

d1 = {'a':1,'b':2,'c':3,'d':4}
for x in d1:
    print(x)
for x in 'ABCD':
    print(x)

L = ['a','b','c']
for i,value in enumerate(L): # 自动添加索引
    print(i,value)

L1 = [(1,1),(2,4),(3,9)]
for x,y in L1:
    print(x,y)
