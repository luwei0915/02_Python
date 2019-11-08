dic = {'a':100,'b':90,'c':80}
print(len(dic))
print(dic['b'])
dic['c']=70
print(dic)

print(dic.get('c'))
print(dic.get('d',999))  # 不存在则给默认值

dic.pop('c')             # 弹出
print(dic)
