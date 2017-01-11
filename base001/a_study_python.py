#!/usr/bin/env python3
# -*- coding: utf-8 -*-

while True:
    print("输入一个字符串:")
    hello = input()
    if hello == 'exit':
        break
    world = hello.replace(" ", "%20")
    print(world)
