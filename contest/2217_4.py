__author_ = "wangqc"
# https://leetcode.com/problems/maximum-points-in-an-archery-competition/

import os
import collections, sortedcontainers, heapq, bisect, math, re
from tkinter import N
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        psum = [list(itertools.accumulate(p, initial=0)) for p in piles]
        n = len(piles)
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(k+1):
                dp[i+1][j] = max(dp[i][j-w] + psum[i][w] for w in range(min(j+1,len(psum[i]))))
        return dp[n][k]

if __name__ == "__main__":
    sol = Solution().maxValueOfCoins

    print(sol(
        piles = [[1,100,3],[7,8,9]], k = 2
    ))

    print(sol(
        piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
    ))

    print(sol(
        piles = [[48,14,23,38,33,79,3,52,73,58,49,23,74,44,69,76,83,41,46,32,28]], k = 10
    ))
