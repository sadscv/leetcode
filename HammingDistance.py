#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-5-12 上午10:09
# @Author  : sadscv
# @File    : HammingDistance.py
import copy


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_str, y_str = self._convert(x), self._convert(y)
        count = 0
        for i in range(31):
            if x_str[i] != y_str[i]:
                count += 1
        return count

    def _convert(self, num):
        string = ''
        for i in range(30, -1, -1):
            string = string + str(num // (2 ** i))
            num = num % (2 ** i)
        return string


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1, 4))
