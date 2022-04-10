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
        M = 10**9+7
        nums.sort()
        i, n = 1, len(nums)
        while i < n:
            gap = (nums[i]-nums[i-1]) * i
            if k < gap:
                break
            k -= gap
            i += 1
        base, leftover = nums[i-1] + k//i, k % i
        p = (pow(base, i-leftover, M) * pow(base+1, leftover, M)) % M
        for x in nums[i:]:
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
