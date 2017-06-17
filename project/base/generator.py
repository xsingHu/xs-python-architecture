#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(pre):
    i, a, b = 0, 0, 1
    while i < pre:
        print(b)
        a, b = b, a + b
        i += 1
    return 'done'

# test
# print(fib(1))

# <generator object gfib at 0x00000259234D78E0>
# generator(生成器); 只能使用一次
def gfib(count):
    c, a, b = 0, 0, 1
    while c < count:
        yield b
        a, b = b, a + b
        c += 1


# test
# print(gfib(10))
# print(list(gfib(10)))
# for n in gfib(10):
#     print(n)
#     pass

# generator 应用场景

# test

# f = fib(5)
# print('fib(10):', f)
# for x in f:
#     print(x)

# call generator manually:
# g = gfib(5)

while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# else

def xx():
    s = (c * c for c in range(5))
    arr = list(s)
    print(arr)
    for b in arr:
        print(b)
        pass
xx()











