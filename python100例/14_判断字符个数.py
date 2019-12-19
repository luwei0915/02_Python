'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''
nums = 0
letters = 0
space = 0
others = 0

s = input("Str:")
for c in s:
    if c.isdigit():
        nums+=1
    elif c.isspace():
        space+=1
    elif c.isalpha():
        letters+=1
    else:
        others+=1
print("数字:%d个,字母%d个,空格%d个,其他字符%d个" %(nums,letters,space,others))
