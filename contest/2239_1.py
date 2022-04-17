__author_ = "wangqc"
# https://leetcode.com/problems/find-closest-number-to-zero/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return min(nums,key=lambda x:(abs(x),-x))

if __name__ == "__main__":
    sol = Solution().findClosestNumber

    print(sol(
        nums = [-4,-2,1,4,8]
    ))

    print(sol(
        nums = [2,-1,1]
    ))
