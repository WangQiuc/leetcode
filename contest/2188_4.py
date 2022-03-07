__author_ = "wangqc"
# https://leetcode.com/problems/minimum-time-to-finish-the-race/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils


class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, n: int) -> int:
        a, dp, mx = [math.inf] * n, [math.inf] * (n+1), 0
        for f, r in tires:
            s, x = changeTime, f
            for i in range(n):
                if x-f > changeTime:
                    mx = max(mx, i+1)
                    break
                a[i] = min(a[i], s:=s+x)
                x *= r
        dp[0] = 0
        for i in range(n):
            for j in range(min(mx,i)+1):
                dp[i+1] = min(dp[i+1], dp[i-j]+a[j])
        return dp[n] - changeTime

if __name__ == "__main__":
    sol = Solution().minimumFinishTime

    print(sol(
        tires = [[2,3],[3,4]], changeTime = 5, n = 4
    ))

    print(sol(
        tires = [[1,10],[2,2],[3,4]], changeTime = 6, n = 5
    ))