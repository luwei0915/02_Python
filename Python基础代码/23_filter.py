def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd,[1,2,3,4,5,6,7]))
print(L)

def not_epmty(s):
    return s and s.strip()

L1 = list(filter(not_epmty,['A','','B',None,'C','  ']))
print(L1)


'''求素数'''
def _odd_iter(): # 无线序列的奇数生成器
    n = 1
    while True:
        n += 2
        yield n

def _not_divisiable(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始化序列 2， 3，5，7，9...
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisiable(n),it)   # 9%3=0 剔除9

for i in primes():
    if i < 100:
        print(str(i) + " ",end='')  # 字符串+ 是拼接
    else:
        break
