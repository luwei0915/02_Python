import os

name = os.name
# nt

d = os.getcwd()
# D:\python\python\01

files = os.listdir()
# ['01_os模块.py', '1.txt']

# os.remove('./1.txt') 直接运行

str = os.path.exists(r"D:\python\python")
# True

str = os.path.isfile('./1.txt')
# True

str = os.path.isdir(r"D:\python\python")
# True

str = os.path.abspath('./1.txt')
# D:\python\python\01\1.txt

str = os.path.split(r"D:\python\python\01\1.txt")
# ('D:\\python\\python\\01', '1.txt')

str = os.path.splitext(r"D:\python\python\01\1.txt")
# ('D:\\python\\python\\01\\1', '.txt')

str = os.path.join(r"D:\python\python","2.txt")
# D:\python\python\2.txt

str = os.path.basename(r"D:\python\python\01\2.txt")
# 2.txt    不管是否真的存在

str = os.path.dirname(r"D:\python\python\02\2.txt")
# D:\python\python\02    不管是否存在

str = os.environ
# environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA':...

str = os.environ["ALLUSERSPROFILE"]
# C:\ProgramData

# os.chdir(r"C:") 直接更换目录

str = os.getlogin()
# 用户名

str = os.getenv('test')
# None

# os.system('cmd')   进入CMD模式

'''
os.name           获取操作系统平台
os.getcwd()       获取现在的工作目录
os.listdir()      获取某个目录下的所有文件名
os.system()       用来运行shell命令
os.remove()       删除某个文件
os.path.exists()  检验给出的路径是否真地存在
os.path.isfile()  判断是否为文件;若是，返回值为真
os.path.isdir()   判断是否为文件夹;若是，返回值为真
os.path.abspath(name)     获得绝对路径
os.path.splitext()        分离文件名与扩展名
os.path.split()           把一个路径拆分为目录+文件名的形式
os.path.join(path,name)   连接目录与文件名或目录
os.path.basename(path)    返回文件名
os.path.dirname(path)     返回文件路径
操作系统相关调用和操作：
os.environ            一个dictionary 包含环境变量的映射关系
os.environ[“HOME”]    可以得到环境变量HOME的值
os.chdir(dir)         改变当前目录 os.chdir(‘d:\outlook’)   注意windows下用到转义
os.getegid()          得到有效组
id os.getgid()        得到组id
os.getuid()           得到用户id
os.geteuid()          得到有效用户id
os.setegid os.setegid() os.seteuid() os.setuid()  设置id
os.getgruops()       得到用户组名称列表
os.getlogin()        得到用户登录名称
os.getenv            得到环境变量
os.putenv            设置环境变量
os.umask             设置umask
os.system(cmd)       利用系统调用，运行cmd命令
'''
