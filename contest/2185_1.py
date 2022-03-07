__author_ = "wangqc"
# https://leetcode.com/problems/counting-words-with-a-given-prefix/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        k = len(pref)
        return sum(w[:k] == pref for w in words)

if __name__ == "__main__":
    sol = Solution().prefixCount

    print(sol(
        words = ["pay","attention","practice","attend"], pref = "at"
    ))

    print(sol(
        words = ["leetcode","win","loops","success"], pref = "code"
    ))