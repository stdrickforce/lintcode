#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


class Solution:

    def adjacent(self, word1, word2):
        if len(word1) != len(word2):
            return False

        distance = 0
        for i in xrange(len(word1)):
            if word1[i] != word2[i]:
                distance += 1
            if distance > 1:
                return False
            i -= 1
        return True

    def findLadders(self, start, end, words):
        from collections import deque, defaultdict

        f = open('words.txt', 'r')
        words = [word.strip() for word in f.readlines()]

        words = [start, end] + list(words)
        length = len(words)
        maps = defaultdict(set)

        for i in xrange(length - 1):
            for j in xrange(i + 1, length):
                if self.adjacent(words[i], words[j]):
                    maps[words[i]].add(words[j])
                    maps[words[j]].add(words[i])

        # bfs search.
        s, minstep, result = deque(), {}, []
        s.append([start])

        a = defaultdict(int)

        while s:
            node = s.popleft()
            step = len(node) + 1
            tail = node[-1]

            a[tail] += 1

            for word in maps[tail]:
                if step > minstep.setdefault(word, 1000):
                    continue
                minstep[word] = min(step, minstep[word])

                if word == end:
                    result.append(node + [end])
                s.append(node + [word])

        return result


print Solution().findLadders('sand', 'acne', [])
