import hashlib

string = 'test'

######## md5 ########
md5 = hashlib.md5()
md5.update(string.encode('utf-8'))     #注意转码
res = md5.hexdigest()
# 098f6bcd4621d373cade4e832627b4f6

######## sha1 ########
sha1 = hashlib.sha1()
sha1.update(string.encode('utf-8'))
res = sha1.hexdigest()
# a94a8fe5ccb19ba61c4c0873d391e987982fbbd3

####### sha256 #######

sha256 = hashlib.sha256()
sha256.update(string.encode('utf-8'))
res = sha256.hexdigest()
# 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08

######## sha384 ######
sha384 = hashlib.sha384()
sha384.update(string.encode('utf-8'))
res = sha384.hexdigest()
# 768412320f7b0aa5812fce428dc4706b3cae50e02a64caa16a782249bfe8efc4b7ef1ccb126255d196047dfedf17a0a9

######### sha512 ########
sha512= hashlib.sha512()
sha512.update(string.encode('utf-8'))
res = sha512.hexdigest()
# ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887
# fd67b143732c304cc5fa9ad8e6f57f50028a8ff

##### 使用byte转换为二进制 #####
sha1 = hashlib.sha1()
sha1.update(bytes(string,encoding='utf-8'))
res = sha1.hexdigest()
# a94a8fe5ccb19ba61c4c0873d391e987982fbbd3

######  m.update(a) m.update(b) = m.update(a+b) #####
m = hashlib.md5()
m.update('a'.encode('utf-8'))
res = m.hexdigest()
# print("第一次a加密:",res)

m.update('b'.encode('utf-8'))
res = m.hexdigest()
# print("第二次b加密:",res)

m1 = hashlib.md5()
m1.update('b'.encode('utf-8'))
res = m1.hexdigest()
# print("b单独加密:",res)

m2 = hashlib.md5()
m2.update('ab'.encode('utf-8'))
res = m2.hexdigest()
# print("ab单独加密:",res)

# 第一次a加密: 0cc175b9c0f1b6a831c399e269772661
# 第二次b加密: 187ef4436122d1cc2f40dc2b92f0eba0
# b单独加密:   92eb5ffee6ae2fec3ad71c777531578f
# ab单独加密: 187ef4436122d1cc2f40dc2b92f0eba0

####### 高级加密 ########
low = hashlib.md5()
low.update('test'.encode('utf-8'))
res = low.hexdigest()
# print("普通加密:",res)
# 098f6bcd4621d373cade4e832627b4f6

high = hashlib.md5(b'test')
high.update('ab'.encode('utf-8'))
res = high.hexdigest()
# print("采用key加密:",res)
# 采用key加密: a9db59a027a68c23b8523fef338e3f03

'''
hash.update(arg) 更新哈希对象以字符串参数
hash.digest() 返回摘要，作为二进制数据字符串值
hash.hexdigest() 返回摘要，作为十六进制数据字符串值
hash.copy() 复制
'''
