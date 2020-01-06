import json

# json.loads

# 1. 常用方法
str1 = '{"a": 123}'                  # a(字符串)必须使用" "包裹，
d1 = json.loads(str1)
# {'a': 123}  字符串格式化为字典

str2 = "{\"a\": 123}"
d2 = json.loads(str2)
# {'a': 123}

# 2 bytes和bytearray数据
str3 = '{"a": 123}'.encode('UTF-8')
d3 = json.loads(str3)
# {'a': 123}

str4 = '{"a": 123}'
d4 = json.loads(bytearray(str4, 'UTF-8'))
# {'a': 123}

str5 = '"hello"'
d5 = json.loads(str5)
# hello  (str)

str6 = '123'
d6 = json.loads(str6)
# 123   (int)

str7 = 'true'
d7 = json.loads(str7)
# True  (<class 'bool'>)

str8 = '[1,2,3]'
d8 = json.loads(str8)
#  [1, 2, 3]   (<class 'list'>)

str9 = '{"a": 123, "b": "ABC", "a": 321}'
d9 = json.loads(str9)
# {'a': 321, 'b': 'ABC'}

with open('./json/js.json') as jf:
    d10 = json.load(jf)
'''
{
# json文件
    "a": 123,
    "b": "ABC",
    "c": [1,2,3,4],
    "d": {"zs": 10,"ls": 20,"ww": 30}
}
'''
# d10 {'a': 123, 'b': 'ABC', 'c': [1, 2, 3, 4], 'd': {'zs': 10, 'ls': 20, 'ww': 30}}
# len(d10)     4
#type(d10)    <class 'dict'>


# 3. 正常转换
str5 = '{"obj":{"zs":10,"ls":20,"ww":30,"zl":40,"arr":[1,2,3],"dic":{"aa":11,"bb":22,"cc":33}}}'
d5 = json.loads(str5)
# {'obj': {'zs': 10, 'ls': 20, 'ww': 30, 'zl': 40, 'arr': [1, 2, 3], 'dic': {'aa': 11, 'bb': 22, 'cc': 33}}}
# type(d5)  <class 'dict'>
# len(d5) 1
# d5["obj"]["dic"]  {'aa': 11, 'bb': 22, 'cc': 33}

# 4 自定义JSON对象转换类型
# object_hook参数可以用来改变构造出的对象.
class myJsObj:
    def __init__(self,x):
        self.x = x

def my_js_obj_hook(data):
    # js_obj data: %s" % data)   {'x': 123}
    return myJsObj(data['x'])
result = json.loads('{"x": 123}',object_hook=my_js_obj_hook)
# type(result)  <class '__main__.myJsObj'>
# result.x    123


'''
json.dumps(): 将字典序列化为json字符串
将json字符串反序列化为字典
json.loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None, 
           parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
json.dump(): 将字典序列化到一个文件，是文本文件，
             就是相当于将序列化后的json字符串写入到一个文件
json.load(): 从文件中反序列出字典

python格式                       json格式
dict（复合类型）                  object
list, tuple（集合类型）           array
int, long, float（数值类型）	   number
str, unicode	                   string
True	                            true
False	                            false
None	                            null

json格式	                      python格式
object	                            dict
array	                            list
string	                            unicode
number(int)	                        int, long
numer(real)	                        float
true	                            True
false	                            False
null	                            None
'''
