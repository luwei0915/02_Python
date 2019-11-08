names=('aa','bb','cc')
print(names)
print(len(names))

L=()
print(len(L))

T=(1,)
print(T)
print(len(T))

names=('aa','bb',['cc','dd'])
print(names)
print(len(names))
names[2][0]='ee'
names[2][1]='ff'
print(names)
