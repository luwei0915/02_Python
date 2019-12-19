import random as rd

# 随机整数
n1 = rd.randint(10,20)
print(n1)

# 随机浮点数
n2 = rd.uniform(10,20)
print(n2)

# 0-1 随机浮点数
n3 = rd.random()
print(n3)

# 1-100 随机奇数
n4 = rd.randrange(1,100,2)
print(n4)

# 随机选取
n5 = rd.choice(['a','b','c'])
print(n5)
