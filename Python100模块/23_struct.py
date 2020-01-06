import struct

s1 = type(b'hello')
# <class 'bytes'>

s2 = type('hello')
# <class 'str'>

# bytes是byte的序列，而str是unicode的序列
# bytes通过decode()方法转换为str类型；str通过encode()方法转换为bytes类型
# 在互联网上是通过二进制进行传输，所以就需要将str通过encode()编码成bytes进行传输，
# 而在接收中通过decode()解码成我们需要的编码进行处理数据这样不管对方是什么编码而本地是我们使用的编码这样就不会乱码

# bytes()是Python3的一个内置函数
s3 = type(bytes())
# <class 'bytes'>
s = bytes()
# b''
s = len(bytes())
# 0

# 写入二进制文件
# file = open('binary.dat','wb')
# for n in range(5):
#     data = struct.pack('i',n)
#     file.write(data)
# file.close()

# s = struct.pack('iii',10,20,30)
# v1,v2,v3 = struct.unpack('iii',s)
# # 10,20,30

# 读取二进制文件
# file = open('binary.dat','rb')
# size = struct.calcsize('i')
# br = file.read(size)
# while br:
#     value = struct.unpack('i',br)
#     value = value[0]
#     print(value,end=' ')
#     br = file.read(size)
# 0 1 2 3 4

'''
对python基本类型值与用python字符串格式表示的C struct类型间的转化
truct模块中的函数
函数	                               return	explain
pack(fmt,v1,v2…)	                   string	按照给定的格式(fmt),把数据转换成字符串(字节流),并将该字符串返回.
pack_into(fmt,buffer,offset,v1,v2…)	None	按照给定的格式(fmt),将数据转换成字符串(字节流),并将字节流写入以
                                                offset开始的buffer中.(buffer为可写的缓冲区,可用array模块)
unpack(fmt,v1,v2…..)	                tuple	按照给定的格式(fmt)解析字节流,并返回解析结果
pack_from(fmt,buffer,offset)	        tuple	按照给定的格式(fmt)解析以offset开始的缓冲区,并返回解析结果
calcsize(fmt)	                        size of fmt	计算给定的格式(fmt)占用多少字节的内存，注意对齐方式
'''
