import json

# json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True,
#            cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

d1 = {'a': 123, 'b': 'ABC'}
js1 = json.dumps(d1)
# {"a": 123, "b": "ABC"}   (<class 'str'>)

d2 = {'数字': 123, '字符': '一二三'}
js2 = json.dumps(d2)
# {"\u6570\u5b57": 123, "\u5b57\u7b26": "\u4e00\u4e8c\u4e09"}  (<class 'str'>)

js3 =  json.dumps(d2,ensure_ascii=False)
# {"数字": 123, "字符": "一二三"}   (<class 'str'>)

d4 = {
    "a": 123,
    "b": "ABC",
    "c": [1,2,3,4],
    "d": {"zs": 10,"ls": 20,"ww": 30}
}
js4 = json.dumps(d4)
# {"a": 123, "b": "ABC", "c": [1, 2, 3, 4], "d": {"zs": 10, "ls": 20, "ww": 30}} <class 'str'>

# 当indent为0或者负数时, JSON字符会包含换行:
d5 = {'a': 123, 'b': {'x': 321, 'y': 'ABC'}}
js5 = json.dumps(d5,indent=-1)
'''
#  括号两头分，: 两边成对出现
{ 
"a": 123,
"b": {
"x": 321,
"y": "ABC"
}

}
'''

# 而当indent为正整数时, 除了换行, JSON还会以指定数量的空格为单位在对象层次间进行缩进
js6 = json.dumps(d4,indent=4)
'''
{
    "a": 123,
    "b": "ABC",
    "c": [
        1,
        2,
        3,
        4
    ],
    "d": {
        "zs": 10,
        "ls": 20,
        "ww": 30
    }
}
'''

# indent还可以是str, 此时, JSON会以str内容为单位进行缩进, 比如制表符\t:
js7 = json.dumps(d5,indent='\t')
'''
{
	"a": 123,
	"b": {
		"x": 321,
		"y": "ABC"
	}
}
'''

# separators可以用来设置输出的分隔符
js8= json.dumps(d5,indent=None,separators=(',', ':'))
# {"a":123,"b":{"x":321,"y":"ABC"}}

# 直接写入文件
# with open('./json/test.json', mode='w') as jf:
#     json.dump(d4, jf,indent='\t')

# json.loads 原型
d6 = json.JSONDecoder().decode('{"a": 123}')
# {'a': 123}   <class 'dict'>

# json.dumps 原型
js9 = json.JSONEncoder().encode({'a': 123})
# {"a": 123}   <class 'str'>
