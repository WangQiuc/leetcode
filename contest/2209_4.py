__author_ = "wangqc"
# https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

import os
import collections, sortedcontainers, heapq, bisect, math, re
from tkinter import N
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def minimumWhiteTiles(self, floor: str, m: int, k: int) -> int:
        n = len(floor)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i, c in enumerate(floor, 1):
            w = c == '1'
            dp[i][0] = dp[i-1][0]+w
            for j in range(1,m+1):
                dp[i][j] = min(dp[i-1][j]+w, dp[max(0,i-k)][j-1])
        return dp[n][m]

if __name__ == "__main__":
    sol = Solution().minimumWhiteTiles

    print(sol(
        floor = "10110101", m = 2, k = 2
    ))

    print(sol(
        floor = "11111", m = 2, k = 3
    ))