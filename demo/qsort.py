#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-9 下午10:11
# @Author  : sadscv
# @File    : qsort.py


def qsort(nums):
    left = []
    right = []
    equal = []
    if len(nums)>1:
        tmp = nums[0]
        for n in nums:
            if n < tmp:
                left.append(n)
            elif n == tmp:
                equal.append(n)
            else:
                right.append(n)
        return qsort(left)+ equal + qsort(right)
    else:
        return nums

if __name__ == '__main__':
    l = [1,2,3,4,2,1,2754,34,24,24,2,52,5]
    r = qsort(l)
    print(r)