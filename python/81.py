#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

from heapq import (
    heappush,
    heappop,
)


class MaxHeap(list):

    def push(self, n):
        heappush(self, -n)

    def pop(self):
        return -heappop(self)


class MinHeap(list):

    def push(self, n):
        heappush(self, n)

    def pop(self):
        return heappop(self)


class Solution:

    def medianII(self, nums):

        median, result = nums[0], [nums[0]]
        minheap, maxheap = MinHeap(), MaxHeap()

        for i in range(1, len(nums)):
            m = nums[i]
            if m > median:
                minheap.push(m)
            else:
                maxheap.push(m)

            if len(maxheap) > len(minheap):
                minheap.push(median)
                median = maxheap.pop()
            elif len(minheap) > len(maxheap) + 1:
                maxheap.push(median)
                median = minheap.pop()
            result.append(median)
        return result


print Solution().medianII([4,5,1,3,2,6,0])
