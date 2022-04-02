__author_ = "wangqc"
# https://leetcode.com/problems/number-of-ways-to-select-buildings/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def numberOfWays(self, s: str) -> int:
        # for each s[i], ans += (number of 1^s[i] on the left) * (number of 1^s[i] on the right)
        n = [s.count('0'), s.count('1')]
        lcnt = [0, 0]
        ans = 0
        for c in s:
            i = c=='0'
            ans += lcnt[i]*(n[i]-lcnt[i])
            lcnt[i^1] += 1
        return ans

if __name__ == "__main__":
    sol = Solution().numberOfWays

    print(sol(
        s = "001101"
    ))

    print(sol(
        s = "11100"
    ))
