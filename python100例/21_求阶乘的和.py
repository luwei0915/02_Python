'''
题目：求1+2!+3!+...+20!的和
'''
s = 0
for i in range(1,21):
    s1 = 1
    for j in range(1,i+1):
        s1 *= j
    s += s1
print(s)
