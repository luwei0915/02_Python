import shutil

'''
将文件内容拷贝到另一个文件中
shutil.copyfileobj(fsrc, fdst[, length])
shutil.copyfileobj(open('./23_test.py','r'), open('./json/test.py', 'w'))(并重命名）

拷贝文件
shutil.copyfile(src, dst)
shutil.copyfile('./23_test.py','./25_test.py')

仅拷贝状态的信息，包括：mode bits, atime, mtime, flags
shutil.copystat(src, dst)  25_test.py必须存在，意思是同步状态信息
shutil.copystat('./23_test.py','./25_test.py')

拷贝文件和权限
shutil.copy(src, dst)
shutil.copy('./23_test.py','./26_test.py')

拷贝文件和状态信息
shutil.copy2(src, dst)
shutil.copy2('./23_test.py','./27_test.py')

递归的去拷贝文件夹
shutil.copytree(src, dst, symlinks=False, ignore=None)
递归拷贝jquery文件夹到新的test文件夹，test文件夹必须不存在
shutil.copytree(r'D:\python\jquery',r'D:\python\python\test')

递归的去删除文件
shutil.rmtree(path[, ignore_errors[, onerror]])
shutil.rmtree('../test')

递归的去移动文件，它类似mv命令，其实就是重命名
shutil.move(src, dst)
shutil.move(r'D:\python\jquery',r'D:\python\jq')

创建压缩包并返回文件路径，例如：zip、tar
shutil.make_archive(base_name, format,...)
base_name： 压缩包的文件名，也可以是压缩包的路径。
format： 压缩包种类，“zip”, “tar”, “bztar”，“gztar”
root_dir： 要压缩的文件夹路径（默认当前目录）
owner： 用户，默认当前用户
group： 组，默认当前组
logger： 用于记录日志，通常是logging.Logger对象
将jq文件夹打包到当前目录下为 jq.tar
shutil.make_archive(r'./jq', 'tar', root_dir=r'D:\python\jq')
'''
