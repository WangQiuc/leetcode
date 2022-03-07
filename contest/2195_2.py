__author_ = "wangqc"
# https://leetcode.com/problems/append-k-integers-with-minimal-sum/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans = k*(k+1)>>1
        p = k+1
        for x in sorted(set(nums)):
            if x < p:
                ans += p-x
                p += 1
        return ans

if __name__ == "__main__":
    sol = Solution().minimalKSum

    print(sol(
        nums = [1,4,25,10,25], k = 2
    ))

    print(sol(
        nums = [5,6], k = 6
    ))