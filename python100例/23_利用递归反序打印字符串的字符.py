'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''
s = input("Input a string:")
l = len(s)

def output(le):
    if le == 0:
        return
    else:
        print(s[le-1])
        output(le - 1)
output(l)
