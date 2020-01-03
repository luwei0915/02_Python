import copy
list1 = [11,22,33,['a','b']]
list2 = list1
list1.append(55)

print(list1)
print(list2)

print(id(list1))      # 内存地址
print(id(list2))      # 指向相同内存地址

print("---------")

list3 = [11,22,33,['a','b']]
list4 = copy.copy(list3)  # 浅拷贝
list3.append(44)

print(list3)
print(list4)

print(id(list3))     # 此时内存地址已经不一样了
print(id(list4))     # 另起一份

print("---------")

c = [11,22,33,['a','b']]    # 深拷贝：复制嵌套列表深层的内存地址，另起一份
d = copy.deepcopy(c)
c[3].append('c')
print(c)
print(d)
