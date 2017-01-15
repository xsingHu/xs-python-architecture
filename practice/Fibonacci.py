#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(haha):
    n, a, b = 0, 0, 1
    while n < haha:
        print(b)
        a, b = b, a + b
        n +=  1
    return 'done'


def gfib(haha):
    c , a, b = 0, 0, 1
    print(c)
    print(a)
    print(b)
    while c < haha:
        yield b
        a, b = b, a + b
        c += 1

for n in gfib(10):
    # print(n)
    pass
