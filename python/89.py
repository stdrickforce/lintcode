#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """

    def kSum(self, A, k, target):

        n = len(A)

        a = [[0] * (target + 1) for j in range(k + 1)]
        a[0][0] = 1

        for i in range(n):
            for v in reversed(range(target + 1)):
                if A[i] > v:
                    break
                for j in range(k):
                    a[j + 1][v] += a[j][v - A[i]]
        return a[k][target]
