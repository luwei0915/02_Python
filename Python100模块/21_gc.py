import gc
import sys

gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)

a=[]
b=[]
a.append(b)
b.append(a)
del a
del b
print(gc.collect())

'''
一.垃圾回收机制
Python中的垃圾回收是以引用计数为主，分代收集为辅。

1、导致引用计数+1的情况
对象被创建，例如a=23
对象被引用，例如b=a
对象被作为参数，传入到一个函数中，例如func(a)
对象作为一个元素，存储在容器中，例如list1=[a,a]

2、导致引用计数-1的情况
对象的别名被显式销毁，例如del a
对象的别名被赋予新的对象，例如a=24
一个对象离开它的作用域，例如f函数执行完毕时，func函数中的局部变量（全局变量不会）
对象所在的容器被销毁，或从容器中删除对象

3、常用函数
gc.set_debug(flags)               设置gc的debug日志，一般设置为gc.DEBUG_LEAK
gc.collect([generation])          显式进行垃圾回收
                                  0代表只检查第一代的对象
                                  1代表检查一，二代的对象
                                  2代表检查一，二，三代的对象
                                  如果不传参数,默认2
gc.get_threshold()                获取的gc模块中自动执行垃圾回收的频率
gc.set_threshold(threshold0[, threshold1[, threshold2]) 设置自动执行垃圾回收的频率
gc.get_count()                     获取当前自动执行垃圾回收的计数器，返回一个长度为3的列表
     第一个数：离上一次一代垃圾检查，Python分配内存的数目减去释放内存的数目
     第二个数：距离上一次二代垃圾检查，一代垃圾检查的次数
     第三个数：距离上一次三代垃圾检查，二代垃圾检查的次数。
     
必须要import gc模块，并且is_enable()=True才会启动自动垃圾回收。
gc模块唯一处理不了的是循环引用的类都有__del__方法，所以项目中要避免定义__del__方法
'''
