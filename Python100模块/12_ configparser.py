import configparser

conf = configparser.ConfigParser()
print(type(conf))                     # conf是类

conf.read('./config.ini')
sections = conf.sections()            # 获取配置文件中所有sections，sections是列表
print(sections)

# 获取某个section下的所有选项或value，等价于 option = conf.options('logoninfo')
option = conf.options(conf.sections()[0])
print(option)

# 根据section和value获取key值,
# 等价于value = conf.get(conf.sections()[0], conf.options(conf.sections()[0])[0])
value = conf.get('loginfo', 'addr')
print(value)

item = conf.items('loginfo')
print(item)
