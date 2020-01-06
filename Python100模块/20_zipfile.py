import zipfile

'''
创建一个zip文件对象，压缩是需要把mode改为'w' 空zip文件
zfile = zipfile.ZipFile("test.zip","w")

将文件写入zip文件中，即将文件压缩
zfile.write('./19_shutil.py')
zfile.write('./16_uuid.py')

将zip文件对象关闭
zfile.close()

解压读取
zfile=zipfile.ZipFile("./test.zip","r")   r表示读取
for file in zfile.namelist():
    print(file)
19_shutil.py
16_uuid.py

解压到指定位置:  ../test
zfile=zipfile.ZipFile("./test.zip","r")
zfile.extractall(path='../test', members=zfile.namelist())

读物第一个文件的内容
zfile=zipfile.ZipFile("./test.zip","r")
text = zfile.read(zfile.namelist()[0]).decode("utf-8")

查看信息
zfile=zipfile.ZipFile("./test.zip","r")
for i in zfile.infolist():
    print(i,i.file_size)
<ZipInfo filename='19_shutil.py' filemode='-rw-rw-rw-' file_size=1728> 1728
<ZipInfo filename='16_uuid.py' filemode='-rw-rw-rw-' file_size=726> 726
'''
