__author_ = "wangqc"
# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        t1 = int(current[:2])*60 + int(current[3:])
        t2 = int(correct[:2])*60 + int(correct[3:])
        gap, ans = t2-t1, 0
        for d in (60,15,5,1):
            ans += gap // d
            gap %= d
        return ans

if __name__ == "__main__":
    sol = Solution().convertTime

    print(sol(
        current = "02:30", correct = "04:35"
    ))

    print(sol(
        current = "11:00", correct = "11:01"
    ))
