'''
题目：
编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
当输入n为奇数时，调用函数1/1+1/3+...+1/n(利用指针函数)
'''

def odd(n):
    s = 0.0
    for i in range(1,n+1,2):
        s += 1 / i
    print(s)

def even(n):
    s = 0.0
    for i in range(2,n+1,2):
        s += 1 / i
    return s

def decall(fp,n):
    s = fp(n)
    return s

if __name__ == '__main__':
    num = int(input("Num:"))
    if num % 2 == 0:
        sum = decall(even,num)
    else:
        sum = decall(odd,num)
    print(sum)
