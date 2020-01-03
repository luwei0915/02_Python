import math
s = math.ceil(7.01)
# 8 向上取整

s = math.floor(9.999)
# 9 向下取整

s = math.pow(2,3)
# 8.0 (底数,幂)

s = math.sqrt(4)
# 2.0 开平方

s = math.fabs(-10)
# 10.0 绝对值

s = math.modf(2.2222222)
# (0.22222220000000004, 2.0)  将一个浮点数拆成整数和小数部分组成的元组

s = math.copysign(12,-40)
# -12.0  将第二个数的正负号复制给第一个数

s = math.fsum((1,2,3,4))
# 10.0  将一个序列的数值进行相加求和 返回浮点型

s = sum((1,2,3,4))
# 10  将一个序列的数值进行相加求和 返回整型

s = math.sin(120)
# 0.5806111842123143

s = math.factorial(5)
# 120  阶乘

s = math.fmod(3,2)
# 1.0 取模运算

s = math.gcd(10,20)
# 10 一键返回最大公约数

s = math.trunc(19.99999)
# 19 截断小数部分

s = math.pi
# 3.141592653589793
