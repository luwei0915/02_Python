l=[1,1,3,3,2,2]
print(l)
s=set(l)
print(s)
print(len(s))

s.add(4)
print(s)

s.remove(3)
print(s)

s.add(3)
print(s)

s1=set([2,3])   #初始化
print(s1)

print(s | s1)   # 合集
print(s & s1)   # 并集
