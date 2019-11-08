print('helo world')

print(100+200)

print('I am','zk','haha')

print('100+200=',100+200)

print(ord('A'))
print(chr(65))

print(len('abc'))
print(len('中国人'))

print('hello,%s,you have $%d.' % ('world',10000))
print('%.2f' % 3.14159)
print('the rate is:%d %%' % 7)

a='abc'
a.replace('a','A')  # replace其实是创建了一个新的字符串，源字符串其实没有改变
b=a.replace('a','A')
print(a)
print(b)

name=input('Please input the name:')
print('hello',name)

print(not True)
