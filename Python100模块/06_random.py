import random

s = random.getstate()
# (3, (2147483648, ...         获得当前状态，用于恢复状态

# random.setstate(state)       用户恢复状态

s = random.getrandbits(10)
#  590                         生成占内存k位以内的随机整数

s = random.random()
# 0.8492897454932434           随机产生一个[0,1.)数字

s = random.uniform(10,20)
# 13.017695101260504           产生一个a、b区间的随机数

s = random.randrange(10,20,2)
# 16                          (start, stop[, step])

s = random.randint(10,20)
# 13                           返回一个[a,b]的随机整数

s = random.choices(['a','b','c'])
# ['c']

s = random.sample(['a','b','c','d'],k=3)
# ['d', 'b', 'a']               随机抽取不重复的k个元素

s = random.shuffle([1,2,3,4])
print(s)
