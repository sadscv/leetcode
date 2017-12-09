#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-6-21 上午11:42
# @Author  : sadscv
# @File    : q121_BestTime_Buy&Sell_Stock.py
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # assert prices
        self.num = prices
        if self.num == []:
            return 0
        self.min = min(self.num)
        self.min_pos = min(range(len(self.num)), key=lambda x: self.num[x])
        self.max = max(self.num[self.min_pos:])
        return self.max - self.min

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """


        # print(self.max, self.min)
        # return self.max - self.min

if __name__ == '__main__':
    nums =  [2,4,1]
    # nums = []
    s = Solution()
    obj = s.maxProfit(nums)
    print(obj)
