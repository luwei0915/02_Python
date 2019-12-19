##############反序输出列表项#################

list = [1,2,3]
for i in list[::-1]:
    print(i)

##############以逗号为分隔符输出列表#########
s = ','.join(str(n) for n in list)
print(s)
