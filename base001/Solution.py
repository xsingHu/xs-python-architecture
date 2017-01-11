# -*- coding:utf-8 -*-

# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

class Solution:
    # array 二维列表
    @staticmethod
    def Find(target, array):

        row = 0
        for i, arr in enumerate(array):
            
            m = int(i/2)
            if target==arr[m]:
                return True
                pass
            elif target>arr[m]:
                pass
            else:
                pass