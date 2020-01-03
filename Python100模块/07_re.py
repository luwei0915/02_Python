import re

s = re.findall('a','aabbb abc abd')
# ['a', 'a', 'a']                 返回所有满足匹配条件的结果,放在列表里

s = re.search('a','aabbb abc abd').group()
# a                               找到则返回，否则None

s = re.match('a','aabbb abc abd').group()
# a                               在字符串开始处进行匹配

s = re.split('[ab]','abcd')
# ['', '', 'cd']                  先按'a'分割得到''和'bcd',再对''和'bcd'分别按'b'分割

s = re.sub('a','A','aabbb abc abd')
# AAbbb Abc Abd                   不指定n，默认替换所有

s = re.sub('a','A','aabbb abc abd',2)
# AAbbb abc abd                   替换n次

s = re.findall('\w', 'ab 12\+- *&_')
# ['a', 'b', '1', '2', '_']       匹配字符数字及下划线

s = re.findall('\W', 'ab 12\+- *&_')
# [' ', '\\', '+', '-', ' ', '*', '&']

s = re.findall('\s','ab 12\+\nz\tz\r- *&_')
# [' ', '\n', '\t', '\r', ' ']

s = re.findall('\S','ab 12\+\nz\tz\r- *&_')
# ['a', 'b', '1', '2', '\\', '+', 'z', 'z', '-', '*', '&', '_']

s = re.findall('cd$','alex is abcd')
# ['cd']

s = re.findall('a.c','abc alc aAc aaaaaaccccsssccc\nc')
# ['abc', 'alc', 'aAc', 'aac']

s = re.findall('ab{2}','abbbb')
# ['abb']

s = re.findall('ab{2,4}','abbbbbb')
# ['abbbb']

s = re.findall('ab{1,}','abbbbbb')
# ['abbbbbb']

s = re.findall('a[1*-]b','a1b a*b a-b')
# ['a1b', 'a*b', 'a-b']

s = re.findall('a[^1*-]b','a1b a*b a-b a=b')
# ['a=b']

s = re.findall('a[0-9]b','a1b a*b a-b a=b')
# ['a1b']

s = re.findall('a[^0-9]b','a1b a*b a-b a=b')
# ['a*b', 'a-b', 'a=b']

s =re.findall('a[a-z]b','a1b a*b a-b a=b aeb')
# ['aeb']

s = re.findall('a[a-zA-Z]b','a1b a*b a-b a=b aeb aEb')
# ['aeb', 'aEb']

s = re.findall(r'a\\c','a\c')
# ['a\\c']
# r代表告诉解释器使用rawstring，即原生字符串，
# 把我们正则内的所有符号都当普通字符处理，不要转义

s = re.findall('ab+','ababab123a')
# ['ab', 'ab', 'ab']

s = re.findall('(ab)+123','aba123bab123a')
# ['ab']                匹配到末尾的ab123a中的ab

s = re.findall('[ab]+123','aba123bab123a123')
['aba123', 'bab123', 'a123']

s = re.findall('href="(.*?)"','<a href="http://www.baidu.com">点击</a>')
# ['http://www.baidu.com']

s = re.findall('compan(?:y|ies)',
'Too many companies have gone bankrupt, and the next one is my company')
# ['companies', 'company']

'''
\w   匹配字符数字及下划线
\W   匹配非字母数字下划线
\s   匹配任意空白字符，等价于[\t\n\r\f]
\S   匹配任意非空白字符
\d   匹配任意数字，等价于[0-9]
\D   匹配任意非数字
\A   匹配字符串开始
\Z   匹配字符串结束，如果是存换行前的结束字符串
\z   匹配字符串结束
\G   匹配最后匹配完成的位置
\n   匹配一个换行符
\t   匹配一个制表符
^    匹配字符串的开头
$    匹配字符串的末尾
.    匹配任意字符，除了换行符，当re.DOTALL标记被指定时，
     则可以匹配包括换行符的任意字符
[...]  用来表示一组字符，单独列出：[amk]匹配'a','m'或'k'
[^...] 不在[]中的字符：[^abc]匹配除了a,b,c之外的字符
*    匹配0个或多个表达式
+    匹配0个或多个的表达式
？   匹配0个或一个由前面的正则表达式定义的片段，非贪婪方式
{n}   精确匹配n个前面的表达式
{n,m} 匹配n到m次由前面的正则表达式定义的片段，贪婪方式
a|b   匹配a或b
()    匹配括号内的表达式，也表示一个组
'''
