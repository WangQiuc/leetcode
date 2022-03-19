__author_ = "wangqc"
# https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

import os
import collections, sortedcontainers, heapq, bisect, math, re
from tkinter import N
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        c1 = c2 = ans = 0
        p1, p2 = pattern
        for c in text:
            if c == p2:
                c2 += 1
                ans += c1
            if c == p1:
                c1 += 1
        return ans + max(c1,c2)


if __name__ == "__main__":
    sol = Solution().maximumSubsequenceCount

    print(sol(
        text = "abdcdbc", pattern = "ac"
    ))

    print(sol(
        text = "aabb", pattern = "ab"
    ))

    print(sol(
        text = "fwymvreuftzgrcrxczjacqovduqaiig", pattern = "yy"
    ))
