import uuid

# Universally Unique Identifier
id1 = uuid.uuid1()
id2 = uuid.uuid4()
id3 = uuid.uuid3(id1,'devil')
id4 = uuid.uuid5(id1,'devil')

# id1  4bc6fd40-2874-11ea-9592-e8d5cd7db597
# id2  008bd7ee-e05f-4554-97e0-10c47f78cbcb
# id3  2310e5ec-b3c8-35a5-bc17-f0654e06c602
# id4  c00509b1-3789-5a24-90a9-35cf9b8fc5b1

'''
uuid.uuid1()
从MAC地址，序列号和当前时间生成UUID，
最后的12个字符对应的就是MAC地址，由此生成可能会暴露MAC地址。

uuid.uuid3()
里面的namespace和具体的字符串都是我们指定的，使用MD5生成UUID

uuid.uuid4()
生成一个随机UUID

uuid.uuid5()
此方法和uuid3写法是一样的，只不过是使用sha1生成UUID
'''
