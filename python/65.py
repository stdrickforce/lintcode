#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


def avg(*args):
    return sum(args) * 1.0 / len(args)


class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """

    def _split(self, a):
        l = len(a)
        m = l / 2

        if l % 2 == 0:
            return l, (a[m - 1] + a[m]) / 2.0
        else:
            return l, a[m] * 1.0

    def _merge(self, A, b):
        al = len(A)
        am = al / 2

        if al == 1:
            return (A[0] + b) / 2.0
        elif al % 2 == 0:
            if b >= A[am]:
                return A[am]
            elif b <= A[am - 1]:
                return A[am - 1]
            return b
        else:
            if b >= A[am + 1]:
                return (A[am] + A[am + 1]) / 2.0
            elif b <= A[am - 1]:
                return (A[am - 1] + A[am]) / 2.0
            return (b + A[am]) / 2.0

    def findMedianSortedArrays(self, A, B):

        if not A:
            return self._split(B)[1]
        if not B:
            return self._split(A)[1]

        al, am = self._split(A)
        bl, bm = self._split(B)

        k = min(al / 2, bl / 2)

        if am == bm:
            return am
        elif al == 1:
            return self._merge(B, A[0])
        elif bl == 1:
            return self._merge(A, B[0])
        elif am > bm:
            return self.findMedianSortedArrays(A[:-k], B[k:])
        elif am < bm:
            return self.findMedianSortedArrays(A[k:], B[:-k])


print Solution().findMedianSortedArrays([], [4, 5, 6, 7])
