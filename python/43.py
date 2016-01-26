#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):

        a, b = [0] + [None] * k, [None] * (k + 1)
        n = len(nums)

        for i in range(n):
            num = nums[i]
            for j in range(k, 0, -1):
                if a[j - 1] is None:
                    continue
                b[j] = max(a[j - 1], b[j]) + num
                a[j] = max(a[j], b[j])
        return a[k]


print Solution().maxSubArray([-1, 4, -2, 3, -2, 3], 2)
