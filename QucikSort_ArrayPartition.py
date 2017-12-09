#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-5-12 上午11:40
# @Author  : sadscv
# @File    : QucikSort_ArrayPartition.py
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = self._qsort(nums)
        sum = 0
        for i in range(2, len(nums)+1, 2):
            sum += nums[-i]
        print(sum)
        return sum

    def _qsort(self, nums):
        left = []
        right = []
        equal = []

        if len(nums) > 1:
            pivot = nums[0]
            for num in nums:
                if num < pivot:
                    left.append(num)
                if num == pivot:
                    equal.append(num)
                if num > pivot:
                    right.append(num)
            return self._qsort(left) + equal + self._qsort(right)
        else:
            return nums

if __name__ == '__main__':
    s = Solution()
    input = [3, 2, 1, 4, 3, 2]
    print(s.arrayPairSum(input))