__author_ = "wangqc"
# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1
        return sum((total-x*cost1)//cost2 + 1 for x in range(total//cost1 + 1))

if __name__ == "__main__":
    sol = Solution().waysToBuyPensPencils

    print(sol(
        total = 20, cost1 = 10, cost2 = 5
    ))

    print(sol(
        total = 5, cost1 = 10, cost2 = 10
    ))
