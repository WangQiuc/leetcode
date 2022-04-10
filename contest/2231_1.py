__author_ = "wangqc"
# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def largestInteger(self, num: int) -> int:
        s = list(map(int,str(num)))
        s1 = sorted(x for x in s if x & 1)
        s2 = sorted(x for x in s if x & 1 == 0)
        ans = ""
        for x in s:
            ans += (str(s1.pop() if x & 1 else s2.pop()))
        return int(ans)

if __name__ == "__main__":
    sol = Solution().largestInteger

    print(sol(
        num = 1234
    ))

    print(sol(
        num = 65875
    ))
