#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


class Solution:
    # @param {string} s the IP string
    # @return {string[]} All possible valid IP addresses

    def validate(self, s):
        if s[0] == '0' and s != '0':
            return False
        return 0 <= int(s) <= 255

    def restoreIpAddresses(self, s):

        # Write your code here
        length, st = len(s), [(0, [])]
        res = []

        while st:

            ptr, t = st.pop()
            if len(t) == 4:
                if ptr == length:
                    res.append(t)
                continue

            for i in range(min(length - ptr, 3), 0, -1):
                segment = s[ptr:ptr + i]
                if self.validate(segment):
                    st.append((ptr + i, t + [segment]))

        return ['.'.join(r) for r in res]


print Solution().restoreIpAddresses('010010')
