__author_ = "wangqc"
# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        lo, hi = 1, sum(candies) // k
        while lo < hi:
            x = lo + hi + 1 >> 1
            if sum(c // x for c in candies) >= k:
                lo = x
            else:
                hi = x - 1
        return hi

if __name__ == "__main__":
    sol = Solution().maximumCandies

    print(sol(
        candies = [5,8,6], k = 3
    ))

    print(sol(
        candies = [2,5], k = 11
    ))
