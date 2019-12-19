'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''
l = []
num = int(input("Num:"))

for i in range(2,num+1):
    while i != num:
        if (num % i == 0):
            num = num / i
            print("%d " % i,end="")
        else:
            break
print(int(num))
