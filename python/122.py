#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        height.append(0)
        length, res, s = len(height), 0, []

        for i in range(length):
            if not s or height[i] >= height[s[-1]]:
                s.append(i)
                continue

            while s and height[i] < height[s[-1]]:
                h = height[s.pop()]
                l = (s[-1] + 1) if s else 0
                res = max(res, (i - l) * h)
            s.append(i)

        return res


# Solution().largestRectangleArea([5, 2, 3, 5, 4, 5, 1, 6])
# print Solution().largestRectangleArea([5, 4, 1, 2])
# print Solution().largestRectangleArea([5, 5, 1, 7, 1, 1, 5, 2, 7, 6])
# print Solution().largestRectangleArea([0, 2, 0])
