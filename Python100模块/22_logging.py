import logging
# logging.basicConfig(
#     filename='app.log',
#     level=logging.DEBUG,
#     format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
#     datefmt='%Y-%m-%d')
# logging.debug('test debug')
# logging.info('test info')
# logging.warning('test warning')
# logging.error('test error')
# logging.critical('test critical')

# 2019-12-30 22_logging.py[line:7] test debug
# 2019-12-30 22_logging.py[line:8] test info
# 2019-12-30 22_logging.py[line:9] test warning
# 2019-12-30 22_logging.py[line:10] test error
# 2019-12-30 22_logging.py[line:11] test critical


a = logging.getLogger('mylogger')
a.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
hdl = logging.StreamHandler()
hdl.setFormatter(formatter)
a.addHandler(hdl)
a.info('test info')



'''
1. 日子模块等级
日志等级 （level）	描述
DEBUG	            最详细的日志信息，典型应用场景是 问题诊断
INFO	            信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
WARNING	            当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
ERROR	            由于一个更严重的问题导致某些功能不能正常运行时记录的信息
CRITICAL	        当发生严重错误，导致应用程序不能继续运行时记录的信息

2. Logging模块提供了两种记录日志的方式：
第一种方式是使用logging提供的模块级别的函数
第二种方式是使用Logging日志系统的四大组件

函数	                              说明
logging.debug(msg, *args, **kwargs)	  创建一条严重级别为DEBUG的日志记录
logging.info(msg, *args, **kwargs)	  创建一条严重级别为INFO的日志记录
logging.warning(msg, *args, **kwargs) 创建一条严重级别为WARNING的日志记录
logging.error(msg, *args, **kwargs)	  创建一条严重级别为ERROR的日志记录
logging.critical(msg, *args, **kwargs)创建一条严重级别为CRITICAL的日志记录
logging.log(level, *args, **kwargs)	  创建一条严重级别为level的日志记录
logging.basicConfig(**kwargs)	      对root logger进行一次性配置

logging模块的四大组件
组件名称	对应类名	功能描述
日志器  	Logger  	提供了应用程序可一直使用的接口
处理器	    handler  	将logger创建的日志记录发送到合适的目的输出
过滤器   	Filter  	提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
格式器  	Formatter 	决定日志记录的最终输出格式

日志器（logger）需要通过处理器（handler）将日志信息输出到目标位置;
不同的处理器（handler）可以将日志输出到不同的位置;
日志器（logger）可以设置多个处理器（handler）将同一条日志记录输出到不同的位置；
每个处理器（handler）都可以设置自己的过滤器（filter）实现日志过滤，从而只保留感兴趣的日志；
每个处理器（handler）都可以设置自己的格式器（formatter）实现同一条日志以不同的格式输出到不同的地方。
日志器（logger）是入口，真正干活儿的是处理器（handler），处理器（handler）
还可以通过过滤器（filter）和格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作。

3. logger类
a = logging.getLogger('mylogger')   getLogger()返回一个logger实例，可以传入一个logger的名字
a.setLevel(logging.INFO)            通过setLeverl()方法可以设置logger的日志输出级别
a.debug('xxxxxx')
a.info('cccccc')                    INFO:mylogger:cccccc

需要之前的logging.basicConfig()的设置，才会输出这个，因为logger的handler还没有加

4. handler类
通过handler对象可以把日志内容写到不同地方，python提供了十几种实用的handler，比较常用的有：
StreamHandler	        输出到控制台
FileHandler	            输出到文件
BaseRotatingHandler 	可以按时间写入到不同的日志中。比如将日志按天写入不同的日期结尾的文件文件
SocketHandler	        用TCP网络连接写LOG
DatagramHandler	        用UDP网络连接写LOG
SMTPHandler	            把LOG写成EMAIL邮寄出去

Handler.setLevel()     设置handler将会处理的日志消息的最低严重级别
Handler.setFormatter() 为handler设置一个格式器对象
Handler.addFilter() 和 Handler.removeFilter()    为handler添加 和 删除一个过滤器对象

5. Formater类
字段/属性名称	使用格式	描述
asctime	        %(asctime)s	日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
created	        %(created)f	日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
relativeCreated	%(relativeCreated)d	日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的）
msecs	        %(msecs)d	日志事件发生事件的毫秒部分
levelname	    %(levelname)s	该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
levelno	        %(levelno)s	该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
name	        %(name)s	所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
message	        %(message)s	日志记录的文本内容，通过 msg % args计算得到的
pathname	    %(pathname)s	调用日志记录函数的源码文件的全路径
filename	    %(filename)s	pathname的文件名部分，包含文件后缀
module	        %(module)s	filename的名称部分，不包含后缀
lineno	        %(lineno)d	调用日志记录函数的源代码所在的行号
funcName	    %(funcName)s	调用日志记录函数的函数名
process	        %(process)d	进程ID
processName	    %(processName)s	进程名称，Python 3.1新增
thread	        %(thread)d	线程ID
threadName	    %(thread)s	线程名称
'''
