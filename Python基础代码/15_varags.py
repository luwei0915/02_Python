def doub(numbers):
    s=0
    for i in numbers:
        s+=i*i
    return s
print(doub([1,2,3]))

def doub1(*numbers):  # 可变参数
    s = 0
    for i in numbers:
        s+=i*i
    return s
print(doub1(1,2,3))

nums=[1,2,3]
print(doub1(*nums))

def person(name,age,**kw): #关键字参数
    print(name,age,kw)
person('zs','30')
person('lisi','29',city='xian',gender='boy')

dic={'a':1,'b':2,'c':3}
person('ww',28,**dic)

def person1(name,age,*,city,job): # 命名关键字参数，只接受*号之后的可选参数
    print(name,age,city,job)
person1('zl',27,city='xian',job='teacher')

def person2(name,age,*,city='xian',job):  #简化调用
    print(name,age,city,job)
person2('zk',12,job='looser')

def f1(a,b,c=0,*args,**kw):
    print(a,b,c,args,kw)
def f2(a,b,c=0,*,d,**kw):  # *是tuple **是dict
    print(a,b,c,d,kw)
f1(1,2,3,'A','B','C',x=99)
f2(1,2,c=10,d=88,num1=99,num2=100)

args = (1,2,3,4)
kw = {'d':99,'x':100,'y':999}
f1(*args,**kw)
args1 = (1,2,3)
f2(*args1,**kw)
