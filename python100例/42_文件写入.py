'''
题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，
然后输出到一个磁盘文件"test"中保存。
'''
if __name__ == '__main__':
    fp = open('../1.txt','a')
    str = input("Str:").upper()
    fp.write(str)
    fp = open('../1.txt','r')
    print(fp.read())
    fp.close()
