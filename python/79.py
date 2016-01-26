#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubstring(self, A, B):
        m, n = len(A), len(B)
        a, res = [0] * n, 0

        for i in range(m):
            for j in reversed(range(n)):
                if B[j] != A[i]:
                    a[j] = 0
                elif j > 0:
                    a[j] = a[j - 1] + 1
                else:
                    a[j] = 1
                res = max(res, a[j])
        return res

Solution().longestCommonSubstring('ABCD', 'DABC')
