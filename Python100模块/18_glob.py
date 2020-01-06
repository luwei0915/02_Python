import glob
name1 = glob.glob(r'D:\python\python\02\*.py')
# ['D:\\python\\python\\02\\12_ configparser.py', 'D:\\python\\python\\02\\13_argparse.py',...

name2 = glob.glob('*.py')
# ['12_ configparser.py', '13_argparse.py',...

name3 = glob.glob('[!^1]*.py')
# ['23_test.py', '24_test.py']      非1开头，以py结尾

name4 = glob.iglob('[!^1]*.py')    # 返回一个迭代器
# <generator object _iglob at 0x00000222873309A8>
#for i in name4:
    #print(i)
# 23_test.py
# 24_test.py

'''
glob模块共包含以下3个函数：

glob(pathname, recursive=False) 
第一个参数pathname为需要匹配的字符串。（该参数应尽量加上r前缀，以免发生不必要的错误） 
第二个参数代表递归调用，与特殊通配符“**”一同使用，默认为False。 
该函数返回一个符合条件的路径的字符串列表，如果使用的是Windows系统，路径上的“\”符号会自动加上转义符号变为“\\”（方便使用）。 
在3.5版本之后，glob函数支持一个特殊的通配符“**”，该通配符可以匹配指定路径里所有文件和目录，包括子目录里的所有文件和目录。
相当于递归地调用了这个函数。使用这个通配符必须加上recursive=True参数。 
（在有复杂目录结构的情况下使用该通配符可能会导致性能下降，拖累整个程序的运行，需谨慎使用！）

iglob(pathname, recursive=False) 
参数与glob()一致。 
返回一个迭代器，该迭代器不会同时保存所有匹配到的路径，遍历该迭代器的结果与使用相同参数调用glob()的返回结果一致。

escape(pathname) 
这个函数是在3.4版本之后才有的，功能是忽略所有通配符。（可以用于测试某文件是否存在） 
（3.5.1版本该函数不能正常运行，升级到3.5.2之后恢复正常）

通配符	功能
*	    匹配0或多个字符
**	    匹配所有文件、目录、子目录和子目录里的文件（3.5版本新增）
?	    匹配1个字符，与正则表达式里的?不同
[exp] 	匹配指定范围内的字符，如：[1-9]匹配1至9范围内的字符
[!exp]	匹配不在指定范围内的字符
'''
