__author_ = "wangqc"
# https://leetcode.com/problems/divide-array-into-equal-pairs/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(v & 1 == 0 for v in collections.Counter(nums).values())

if __name__ == "__main__":
    sol = Solution().divideArray

    print(sol(
        nums = [3,2,3,2,2,2]
    ))

    print(sol(
        nums = [1,2,3,4]
    ))
