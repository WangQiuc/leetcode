__author_ = "wangqc"
# https://leetcode.com/problems/maximum-product-after-k-increments/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        a = sorted(nums)
        i, n = 1, len(a)
        while i < n:
            gap = (a[i]-a[i-1]) * i
            if k < gap:
                break
            k -= gap
            i += 1
        base, leftover = a[i-1] + k//i, k % i
        for j in range(i):
            a[j] = base + (j < leftover)
        p, M = 1, 10**9+7
        for x in a:
            p = (p*x) % M
        return p

if __name__ == "__main__":
    sol = Solution().maximumProduct

    print(sol(
        nums = [0,4], k = 5
    ))

    print(sol(
        nums = [6,3,3,2], k = 2
    ))
