#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-9 下午11:25
# @Author  : sadscv
# @File    : q88_mergeSort.py


def merge(num1, num2):
    num1 = sorted(num1)
    num2 = sorted(num2)
    i, j = 0, 0
    result = []
    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            result.append(num1[i])
            i += 1
        else:
            result.append(num2[j])
            j += 1
    result += num1[i:]
    result += num2[j:]
    return result

def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    half = len(nums)//2
    left = mergeSort(nums[:half])
    right = mergeSort(nums[half:])
    return merge(left, right)

if __name__ == '__main__':
    num1 = [1,23,5,36,457,4,583585,23, 3]
    num2 = [4352,42,42,42,2,412,987,4,5,2,9,1]
    print(merge(num1, num2))
    print(mergeSort(num1))
