names=['zs','ls','ww']
print(names)
print(len(names))
print(names[0])
print(names[-1])     # 最后一个数
print(names[-2])     # 倒数第二个数

names.append('aa')   #末尾追加
print(names)

names.insert(4,'bb')  #指定位置插入
print(names)

names.pop()           # 末尾删除
print(names)

names.pop(0)          # 指定位置删除
print(names)

names[0]='zs'        # 指定位置替换
print(names)

L=[]                 # 空列表
print(len(L))
