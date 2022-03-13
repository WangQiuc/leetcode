__author_ = "wangqc"
# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

import os
import collections, sortedcontainers, heapq, bisect, math, re
from tkinter import N
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1 and (k & 1):
            return -1
        ans = max(nums[:(min(max(0,k-1),n))], default=-1)
        return max(ans,nums[k]) if k < n else ans

if __name__ == "__main__":
    sol = Solution().maximumTop

    print(sol(
        nums = [5,2,2,4,0,6], k = 4
    ))

    print(sol(
        nums = [2], k = 1
    ))

    print(sol(
        nums = [2], k = 2
    ))