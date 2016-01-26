#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        m, n = len(A), len(B)
        a = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    a[i][j] = a[i - 1][j - 1] + 1
                else:
                    a[i][j] = max(a[i - 1][j], a[i][j - 1])
        return a[m][n]


Solution().longestCommonSubsequence('ABCD', 'EACB')
