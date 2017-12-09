#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-6-21 上午10:52
# @Author  : sadscv
# @File    : q303_RangeSumQuery.py

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        num = self.nums[i:j + 1]
        return sum(num)


# Your NumArray object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    param_1 = obj.sumRange(0, 5)
    print(param_1)
