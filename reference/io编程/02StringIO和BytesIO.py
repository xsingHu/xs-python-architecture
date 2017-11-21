#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


"""

# StringIO
from io import StringIO, BytesIO

"""
很多时候，数据读写不一定是文件，也可以在内存中读写。

StringIO顾名思义就是在内存中读写str。

要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可
"""

f = StringIO()
f.write('hello world')
f.write(' ')
f.write('哈哈')

print(f.getvalue())

f = StringIO('hello!\nHi!\nGoodbye')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


# BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))

print(f.getvalue())

# 小结:StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。