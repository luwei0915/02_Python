def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n+=1
    return 'done'

def fib1(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n+=1
    return 'done'

fib(5)
print('------------------------')
for i in fib1(5):
    print('fib1',i)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
o=odd()
for i in o:
    print(i)
'''list dict,str 都是Iterable（可迭代对象）,但不是Iterator（迭代器）,可以通过iter()函数获得一个Iterator对象
   it = iter([1,2,3])
'''
