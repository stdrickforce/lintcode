#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here

        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        a = [[False] * (n + 1) for i in range(m + 1)]
        a[0][0] = True

        for i in range(m):
            a[i + 1][0] = s3[i] == s1[i]

        for j in range(n):
            a[0][j + 1] = s3[j] == s2[j]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                a[i][j] = \
                    (a[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                    (a[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return a[m][n]


s = Solution()
print s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
