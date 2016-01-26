#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string

    def adjacent(self, word1, word2):
        if len(word1) != len(word2):
            return False

        distance, i = 0, 0
        while i < len(word1):
            if word1[i] != word2[i]:
                distance += 1
            if distance > 1:
                return False
            i += 1
        return True

    def ladderLength(self, start, end, words):

        f = open('words.txt', 'r')
        words = [word.strip() for word in f.readlines()]

        words = [start, end] + list(words)
        length = len(words)

        from collections import defaultdict
        maps = defaultdict(set)

        for i in range(length - 1):
            for j in range(i + 1, length):
                if self.adjacent(words[i], words[j]):
                    maps[words[i]].add(words[j])
                    maps[words[j]].add(words[i])

        # dfs search.
        from collections import deque
        s, minstep, result = deque(), {}, []
        s.append([start])

        while s:
            node = s.popleft()
            step = len(node) + 1
            tail = node[-1]

            for word in maps[tail]:
                if step > minstep.setdefault(word, 1000):
                    continue

                if step < minstep[word]:
                    minstep[word] = step
                    if word == end:
                        result = []

                if word == end:
                    result.append(node + [end])
                s.append(node + [word])

        return result


print Solution().ladderLength('sand', 'acne', [])
print Solution().ladderLength('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log'])
