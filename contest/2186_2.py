__author_ = "wangqc"
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

import os
import collections, sortedcontainers, heapq, bisect, math, re, string
import functools, itertools
import random, sys
from typing import List

from utils import Utils


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = collections.Counter(s), collections.Counter(t)
        return sum(abs(c1[c]-c2[c]) for c in string.ascii_lowercase)

if __name__ == "__main__":
    sol = Solution().minSteps

    print(sol(
        s = "leetcode", t = "coats"
    ))

    print(sol(
        s = "night", t = "thing"
    ))