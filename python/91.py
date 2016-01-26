#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

MAX = 100


class Solution:

    # @param A: An integer array.
    # @param target: An integer.
    def MinAdjustmentCost(self, A, target):

        for i in range(MAX):
            a = [abs(A[0] - i - 1) for i in range(MAX)]

        for i in range(1, len(A)):
            b = [0] * MAX
            for j in range(MAX):
                diff = abs(A[i] - j - 1)
                s = max(j - target, 0)
                t = min(j + target, MAX - 1)
                b[j] = min(a[k] + diff for k in range(s, t + 1))
            a = b

        return min(a)


print Solution().MinAdjustmentCost([12,3,7,4,5,13,2,8,4,7,6,5,7], 2)
