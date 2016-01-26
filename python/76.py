#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        n = len(nums)

        a, res = [1] * n, 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] >= nums[j]:
                    a[i] = max(a[i], a[j] + 1)
                    res = max(a[i], res)
        return res


print Solution().longestIncreasingSubsequence([88,4,24,82,86,1,56,74,71,9,8,18,26,53,77,87,60,27,69,17,76,23,67,14,98,13,10,83,20,43,39,29,92,31,0,30,90,70,37,59])
