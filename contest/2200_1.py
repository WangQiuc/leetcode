__author_ = "wangqc"
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = [-1]
        idx = [i for i, x in enumerate(nums) if x == key]
        n = len(nums)
        for i in idx:
            ans += list(range(max(ans[-1]+1, i-k), min(i+k+1, n)))
        return ans[1:]

if __name__ == "__main__":
    sol = Solution().findKDistantIndices

    print(sol(
        nums = [3,4,9,1,3,9,5], key = 9, k = 1
    ))

    print(sol(
        nums = [2,2,2,2,2], key = 2, k = 2
    ))
