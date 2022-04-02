__author_ = "wangqc"
# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal).count('1')

if __name__ == "__main__":
    sol = Solution().minBitFlips

    print(sol(
        start = 10, goal = 7
    ))

    print(sol(
        start = 3, goal = 4
    ))
