__author_ = "wangqc"
# https://leetcode.com/problems/sum-of-scores-of-built-strings/

import os
import collections, sortedcontainers, heapq, bisect, math, re
from tkinter import N
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def sumScores(self, s: str) -> int:
        l, r, n = 0, 0, len(s)
        z = [0] * n
        for i in range(1,n):
            if i <= r:
                z[i] = min(z[i-l], r-i+1)
            while i+z[i] < n and s[z[i]] == s[i+z[i]]:
                z[i] += 1
            if i+z[i]-1 > r:
                l, r = i, i+z[i]-1
        return sum(z) + n

if __name__ == "__main__":
    sol = Solution().sumScores

    print(sol(
        s = "babab"
    ))

    print(sol(
        s = "azbazbzaz"
    ))
