#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. 切片

2.迭代

3.列表生成式

4.生成器

5.迭代器


"""

# 切片
import os
from collections import Iterable

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[:1])
print(L[-3:4])
print(L[-1:])
# 从1开始 每3个取一个
print(L[1::3])

# 迭代
ch = "hello world"
for c in ch:
    print(c)

d = {'a': 1, 'b': 2}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k + " :" + str(v))

print(isinstance('abc', Iterable))

print("# 下标")
for i, value in enumerate(ch):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)



print("------# 列表生成式 ")

print(list(range(1,11)))

print([x*x for x in  range(1,11)])

print([x*x for x in range(1,11) if x%2 == 0])

print([m+n for m in 'ABC' for n in 'XYZ'])

print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 1]
print([s.lower() for s in L if isinstance(s ,str)])


print("------# 生成器 generator ")
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator

g = (x*x for x in range(10))
next(g)

for n in g:
    print(n)

# 定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(10)
for n in f:
    print(n)

g = fib(10)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Gererator return value:',e.value)
        break

print('# 迭代器 -------------')
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator

# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

"""
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的
"""


