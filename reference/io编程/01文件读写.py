#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。

"""
# 以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符   文本

with open('/path/to/file', 'r') as f:
    print(f.read())

"""
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
"""

for line in f.readlines():
    print(line.strip())  # 把末尾的'\n'删掉

"""
像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行
"""

# 二进制文件  前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可

f = open('/Users/michael/test.jpg', 'rb')
f.read()


# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')

# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()

# with open('/Users/michael/test.txt', 'w') as f:
#     f.write('Hello, world!')











































