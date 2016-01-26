#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here

        n = len(s)

        f = [[False] * n for i in xrange(n)]
        for i in xrange(1, n):
            f[i][i] = True
            f[i - 1][i] = s[i - 1] == s[i]
        f[0][0] = True

        for step in xrange(2, n):
            for i in xrange(n):
                if i + step >= n:
                    break
                f[i][i + step] = s[i] == s[i + step] and f[i + 1][i + step - 1]

        a = [0] * n
        a[0] = 1
        for i in xrange(1, n):
            if f[0][i]:
                a[i] = 1
            else:
                a[i] = min(a[j] + 1 for j in xrange(i) if f[j + 1][i])
        return a[n - 1] - 1


print Solution().minCut('aab')
