functools import reduce
def f(x):
    return x*x
L = []
for i in list(range(1,9)):
    L.append(f(i))
print(L)

m = map(f,list(range(1,9)))  # 第一个参数是方法，第二个参数是Iterator
print(list(m))

L1 = list(map(str,[1,2,3])) # 一条命令搞定 将数字转化为字符串
print(L1)

print('--------------------------')
'''作用类似：reduce(f,[x1,x2,x3]) = f(f(f(x1,x2),x3),x4)，必须接受两个参数'''
def add(x,y):
    return x+y

print(reduce(add,[1,2,3]))

def fn(x,y):
    return x * 10 + y

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
num = reduce(fn,map(char2num,'13579')) # {"1":1, "2":2}["1"] = 1
print(num)
