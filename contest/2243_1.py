__author_ = "wangqc"
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = "".join(str(sum(int(x) for x in s[i:i+k])) for i in range(0,len(s),k))
        return s

if __name__ == "__main__":
    sol = Solution().digitSum

    print(sol(
        s = "11111222223", k = 3
    ))

    print(sol(
        s = "00000000", k = 3
    ))
