#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：
"""


# python language reference 语法参考:包括基本语法的一个完整例子

# Python（英国发音：/ˈpaɪθən/ 美国发音：/ˈpaɪθɑːn/）, 是一种面向对象的解释型计算机程序设计语言，由荷兰人Guido van Rossum于1989年发明，第一个公开发行版发行于1991年。
# Python是纯粹的自由软件， 源代码和解释器CPython遵循 GPL(GNU General Public License)协议 。

# python的指导思想是:对于一个特定的问题,只要有一种最好的方法来解决就好了.
# There should be one-- and preferably only one --obvious way to do it.

# Python的设计哲学是“优雅”、“明确”、“简单”。

# Python是完全面向对象的语言。函数、模块、数字、字符串都是对象。
# 并且完全支持继承、重载、派生、多继承，有益于增强源代码的复用性。
# Python支持重载运算符和动态类型。相对于Lisp这种传统的函数式编程语言，Python对函数式设计只提供了有限的支持。
# 有两个标准库(functools, itertools)提供了Haskell和Standard ML中久经考验的函数式程序设计工具。

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
import time
import sys

print("Your Story may not have such a happy beginning, but that doesn't make who you are. It is the rest of your story, who you choose to be.")
print("你人生故事的开头也许不那么快乐,但是这并不能影响你成为什么样的人,关键看后来的人生路,你选择怎么走下去\n")

# 系统参数输入
path = sys.argv[0]
print("path:"+path)

# 输入
get = input("请输入:\n")
print(get)

# 变量类型
"""
    在python中能够直接处理的数据类型(基本数据类型)有:
        整数
        浮点数 1.23，3.14，-9.01  1.23e9  1.2e-5
        字符串 ""
        布尔值 True False
        空值 None
    此外还有 列表,字典等  以及自定义数据类型
"""
# 变量  or  常量
"""
    所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量
    Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。
"""
# 运算符
# 除法
"""
/  除法    计算结果是浮点数,所以除法是精确的(两个整数的除法也是浮点数).    10 / 3 = 3.3333333333333335
// 地板除  两个整数的除法仍然是整数 11//3 = 3  取整数部分
%  取余    取余数部分 11%3 = 2
"""

# 字符编码
"""
现在计算机系统通用的字符编码工作方式：
    在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件
    'ABC'.encode('ascii')
    '中文'.encode('utf-8')
Python对bytes类型的数据用带b前缀的单引号或双引号表示：x = b'ABC'
"""

# 条件语句--循环语句--While循环语句--for循环语句--循环嵌套--break语句--continue语句--pass语句

# 序列(序列是Python中最基本的数据结构:序列中的每个元素都分配一个索引0,1,...)

# 包含6个序列的内置类型(列表,元组,字典...)

# 序列都可以进行的操作包括索引，切片，加，乘，检查成员。

# 列表 List
list1 = ['hello', 'world', 'you', 'good', 'nice']
# 访问列表中的值
print(list1[0] + ' ' + list1[1])
print(list1[2:4])  # 切片

# 更新列表中的值
list1[1] = 'zhangsan'
print(list1)

# 添加元素
list1.append('very')
print(list1)

# 删除元素
list1.remove('zhangsan')
list1.__delitem__(0)
print(list1)

# 元组 (元组的元素不同修改,其他与列表同)元组使用小括号，列表使用方括号。
tup1 = ('hello', 'world')
tup2 = "a", "b", "c", "d";
tup3 = ();  # 创建空元组
tup4 = (50,);  # 元组中只包含一个元素时，需要在元素后面添加逗号
print(tup2)

# 字典(Dictionary) 字典是另一种可变容器模型，且可存储任意类型对象。
d = {'key1': 1, 'key2': 'hello'}
dict2 = {'abc': 123, 98.6: 37};
print(d)
print(dict2)
print(d['key1'])
d['key1'] = 2

# 日期和时间
ticks = time.time()
print('当前的时间戳为:', ticks)
localtime = time.localtime(time.time())
print('本地时间为:', localtime, '\n')
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
