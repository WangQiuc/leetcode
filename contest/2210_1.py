__author_ = "wangqc"
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def countHillValley(self, A: List[int]) -> int:
        p, cnt = A[0], 0
        for i, x in enumerate(A[2:],1):
            if (p < A[i] > x) or (p > A[i] < x):
                cnt += 1
                p = A[i]
        return cnt

if __name__ == "__main__":
    sol = Solution().countHillValley

    print(sol(
        A = [2,4,1,1,6,5]
    ))

    print(sol(
        A = [6,6,5,5,4,1]
    ))
