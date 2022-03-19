__author_ = "wangqc"
# https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

import os
import collections, sortedcontainers, heapq, bisect, math, re
from tkinter import N
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        t = sum(nums) / 2
        pq = [-x for x in nums]
        heapq.heapify(pq)
        s = ans = 0
        while s < t:
            x = heapq.heappop(pq)
            s -= x / 2
            heapq.heappush(pq, x/2)
            ans += 1
        return ans


if __name__ == "__main__":
    sol = Solution().halveArray

    print(sol(
        nums = [5,19,8,1]
    ))

    print(sol(
        nums = [3,8,20]
    ))
