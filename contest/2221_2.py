__author_ = "wangqc"
# https://leetcode.com/problems/find-triangular-sum-of-an-array/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def triangularSum(self, A: List[int]) -> int:
        n = len(A)
        for i in range(n-1,0,-1):
            for j in range(i):
                A[j] = (A[j]+A[j+1]) % 10
        return A[0]

if __name__ == "__main__":
    sol = Solution().triangularSum

    print(sol(
        A = [1,2,3,4,5]
    ))

    print(sol(
        A = [5]
    ))
