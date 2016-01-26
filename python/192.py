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
    def isMatch(self, s, p):

        if not p:
            return False
        if not s:
            if p == '*':
                return True
            return False

        m, n = len(s), len(p)
        f = [[False] * n for i in range(m)]

        if p[0] == '*':
            for i in range(m):
                f[i][0] = True
        elif p[0] == '?' or p[0] == s[0]:
            f[0][0] = True

        for j in range(1, n):
            for i in range(1, m):
                if p[j] == '*':
                    f[i][j] = max(f[x][j - 1] for x in range(i))
                elif p[j] == '?' or p[j] == s[i]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = False
        return f[m - 1][n - 1]


print Solution().isMatch('bbabacccbcbbcaaab', '*a*b??b*b')
