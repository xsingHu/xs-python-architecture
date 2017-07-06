#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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


def main():
    print(
        "Your Story may not have such a happy beginning, but that doesn't make who you are. It is the rest of your story, who you choose to be.")
    print("你人生故事的开头也许不那么快乐,但是这并不能影响你成为什么样的人,关键看后来的人生路,你选择怎么走下去\n")
    # 输出
    print('hello,python!这里我们将看到python基本的语法规则.\n')

    # 变量类型--运算符
    # 条件语句--循环语句--While循环语句--for循环语句--循环嵌套--break语句--continue语句--pass语句


    # 序列(序列是Python中最基本的数据结构:序列中的每个元素都分配一个索引0,1,...)--包含6个序列的内置类型(列表,元组,...);
    # 序列都可以进行的操作包括索引，切片，加，乘，检查成员。

    # 列表 Lists
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

# 函数
"""
你可以定义一个由自己想要功能的函数，以下是简单的规则：
    函数代码块以def关键词开头，后接函数标识符名称和圆括号()。
    任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号起始，并且缩进。
    Return[expression]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""


# 函数定义
def func1(param):
    print(str(param))



func1("hello world!")

# 函数参数的类型和应用场景
# 调用函数
main()
