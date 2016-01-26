#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: A boolean
    """

    def equal(self, x, y):
        if x == '.' or y == '.':
            return True
        return x == y

    def isMatch(self, s, p):

        m, n = len(s), len(p)
        f = [[False] * n for i in range(m)]

        for j in range(n):
            if p[j] == '*':
                continue
            for i in range(m):
                if self.equal(s[i], p[j]):
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = False
        return f[m - 1][n - 1]


print Solution().isMatch('bbabacccbcbbcaaab', 'c*a*b')
