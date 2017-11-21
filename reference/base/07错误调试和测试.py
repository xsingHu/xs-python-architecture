#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. 切片

2.迭代

3.列表生成式

4.生成器

5.迭代器


"""
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(100))
