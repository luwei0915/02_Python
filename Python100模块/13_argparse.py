import argparse
'''
1. 命令行框架
parser = argparse.ArgumentParser(description="程序的主要功能是...")
parser.parse_args()
执行:
    python D:\python\python\02\13_argparse.py --help
结果：
        usage: 13_argparse.py [-h]
        程序的主要功能是...
        optional arguments:
            -h, --help  show this help message and exit

2. 添加一个位置参数
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print('参数echo的值是{}'.format(args.echo))
执行:
    python D:\python\python\02\13_argparse.py 'hello'
结果：
    参数echo的值是hello

3. 为位置参数添加说明
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="我是关于echo的说明")
args = parser.parse_args()
print('参数echo的值是{}'.format(args.echo))
执行:
    python D:\python\python\02\13_argparse.py -h
结果：
    positional arguments:
        echo        我是关于echo的说明
    optional arguments:
        -h, --help  show this help message and exit

4. 指定参数类型
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int)
args = parser.parse_args()
print(args.square**2)
执行:
    python D:\python\python\02\13_argparse.py 123
结果：
    15129
注意这里的代码指定了一个位置参数square，并且指定类型为int。
默认情况下，如果没有指定类型，argparse会将参数作为字符串存储。

5. 指定可选参数
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity")
args = parser.parse_args()
print('可选参数verbosity的值是{}'.format(args.verbosity))
执行:
    python D:\python\python\02\13_argparse.py --verbosity 123
结果：
    可选参数verbosity的值是123
    
注意，在参数前加上前缀--，即意味着这个参数是可选参数。
可选参数与位置参数有两点不同：
第一，可选参数可以不指定,可选参数verbosity的值是None

6. 设定无需具体值参数
比如说我们想要设定一个参数，如果指定了该参数，就执行一个功能，
如果没指定，则不执行。具体该参数的值是多少在所不问。

arser = argparse.ArgumentParser()
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()
print("参数verbose的值是{}".format(args.verbose))
执行:
    python D:\python\python\02\13_argparse.py --verbosity
结果：
    参数verbose的值是True
    
可以看到，在执行代码时，指定了可选参数--verbose，但是没有指定verbose的值。
此时verbose的值就默认为布尔值True。
实现这一目的的方法是将action参数的值指定为 "store_true"。
通过这个特点，就可以实现使用某一个特定功能这个目的。


7. 设定参数的简短形式
上面我们可以注意到，-h 是 --help 和简单形式，二者功能相同。
我们也可以为自己设定的参数指定简短的形式。

parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbose", action="store_true")
args = parser.parse_args()
print("参数verbose的值是{}".format(args.verbose))
执行:
    python D:\python\python\02\13_argparse.py -v
结果：
    参数verbose的值是True
说明，在可选参数前添加一个简短的参数，与直接使用原参数效果相同。

8.  同时添加位置参数和可选参数
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int)
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()
if args.verbose:
    print("the square of {} equals {}".format(args.square, args.square**2))
else:
    print(args.square**2)
执行方式1:
    python D:\python\python\02\13_argparse.py 50
结果：
    2500

执行方式2:
    python D:\python\python\02\13_argparse.py 50 -v
结果：
    the square of 50 equals 2500
通过多次使用add_argument方法，来添加多个命令行参数。

9. 为可选参数设置取值范围
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2])
args = parser.parse_args()
print("可选参数verbosity的值为{}".format(args.verbosity))

多次不同方式执行代码：
python 13_argparse.py
可选参数verbosity的值为None

python 13_argparse.py -v 1
可选参数verbosity的值为1

python 13_argparse.py -v 2
可选参数verbosity的值为2

python 13_argparse.py -v 3
usage: 13_argparse.py [-h] [-v {0,1,2}]
13_argparse.py: error: argument -v/--verbosity: invalid choice: 3 (choose from 0, 1, 2)

10. 监控可选参数的执行次数
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", action="count")
args = parser.parse_args()
print("可选参数verbosity的值为{}".format(args.verbosity))
执行：
    python 1.py -v
    可选参数verbosity的值为1

    python 1.py -vv
    可选参数verbosity的值为2

    python 1.py -vvvvv
    可选参数verbosity的值为5

    python 1.py
    可选参数verbosity的值为None
    
11. 设置参数的默认值
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", default=0)
args = parser.parse_args()
print("可选参数verbosity的值为{}".format(args.verbosity))

不同方式多次执行：
    python 1.py
    可选参数verbosity的值为0
    python 1.py -v 100
    可选参数verbosity的值为100
    
12 设置冲突参数
冲突参数是指，两个参数只能二选其一。
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
args = parser.parse_args()
print("可选参数verbosity的值为{}".format(args.verbose))
print("可选参数quiet的值为{}".format(args.quiet))
不同方式多次执行：
    python 1.py  
        可选参数verbosity的值为False
        可选参数quiet的值为False
    python 1.py -q
        可选参数verbosity的值为False
        可选参数quiet的值为True
    python 1.py -v
        可选参数verbosity的值为True
        可选参数quiet的值为False
    python 1.py -v -q
    1.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
    usage: 1.py [-h] [-v | -q]
    
    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose
      -q, --quiet
'''
