#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。


"""


import os

print(os.name)

# print(os.uname()) Windows不提供

print(os.environ.get('PATH'))

# 操作文件和目录
currentPath = os.path.abspath('.')
print(currentPath)

newPath = os.path.join(currentPath,'testdir')

print(newPath)

# os.mkdir(newPath)
# os.rmdir(newPath)
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数
current_file = os.path.join(currentPath,'03操作文件和目录.py')
# 拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
print(os.path.split(current_file))
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便
print(os.path.splitext(current_file))

# shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充

# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。


