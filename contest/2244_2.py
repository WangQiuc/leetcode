__author_ = "wangqc"
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ctr = collections.Counter(tasks)
        s = 0
        for n in ctr.values():
            if n == 1:
                return -1
            s += (n-1)//3+1
        return s

if __name__ == "__main__":
    sol = Solution().minimumRounds

    print(sol(
        tasks = [2,2,3,3,2,4,4,4,4,4]
    ))

    print(sol(
        tasks = [2,3,3]
    ))
