#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


class Solution:
    # array 二维列表

    def Find(target, array):
        index = len(array)-1
        jndex = 0
        while True:
            if jndex == len(array[0]) or index < 0:
                return False
            print(array[index][jndex])
            if target == array[index][jndex]:
                print("存在目标:" + str(target) + " i:" + str(index) + " j:" + str(jndex))
                return True
            elif target < array[index][jndex]:
                index -= 1
            else:
                jndex += 1
        return False







