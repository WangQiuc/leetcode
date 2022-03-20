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
    def maximumBobPoints(self, n: int, A: List[int]) -> List[int]:
        S = (1<<11)-1
        ans = best_score = 0
        for s in range(S,0,-1):
            k = sum(A[i+1]+1 for i in range(11) if (s>>i&1))
            score = sum(i+1 for i in range(11) if (s>>i&1))
            if k <= n and score > best_score:
                ans, best_score = s, score
        B = [A[i+1]+1 if (ans>>i&1) else 0 for i in range(11)]
        return [n-sum(B)] + B


if __name__ == "__main__":
    sol = Solution().maximumBobPoints

    print(sol(
        n = 9, A = [1,1,0,1,0,0,2,1,0,1,2,0]
    ))

    print(sol(
        n = 3, A = [0,0,1,0,0,0,0,0,0,0,0,2]
    ))
