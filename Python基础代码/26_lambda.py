L = list(map(lambda x:x*x ,[1,3,5,7,9]))
print(L)

def log(func):   # 装饰器
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log        # 相当于执行了now = log(now)
def now():  # 不改变原函数或者类的情况下为其增加或者修改功能
    print(2019)

n = now
n()
print(now.__name__)
print(n.__name__)

'''
import functools   # 无参数
def log(func):
    @functools.wraps(func)
    def wrapper(*args,kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

import functools     # 带参数
def log(text):
    def decorator(func):
          @functools.wraps(func)
          def wrapper(*args,kw):
              print('%s %s():' % (text,func.__name__))
              return func(*args,**kw)
          return wrapper
    return decorator

'''
