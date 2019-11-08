def my_abs(x):
    if not isinstance(x,(int,float)):  # 如果不是给定类型的话，自定义抛出错误
        raise TypeError('Type Wrong')
    if x >= 0:
        return x
    else:
        return  -x

a=int(input('input a num:'))
print(my_abs(a))

a='a'
print(my_abs(a))
