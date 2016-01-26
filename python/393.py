#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


class Solution:
    """
    @param k: an integer
    @param prices: a list of integer
    @return: an integer which is maximum profit
    """
    def maxProfit(self, k, prices):
        # write your code here

        n = len(prices)
        l = [prices[i + 1] - prices[i] for i in range(n - 1)]
        l = filter(lambda x: x > 0, l)

        if k > len(l):
            return sum(l)

        a = [0] * (k + 1)
        b = [0] * (k + 1)

        for i in range(2, n + 1):
            delta = prices[i - 1] - prices[i - 2]
            for j in range(k, 0, -1):
                b[j] = max(a[j - 1], b[j]) + delta
                a[j] = max(a[j], b[j])
        return a[k]


print Solution().maxProfit(1, [4, 4, 6, 1, 1, 4, 2, 5])
