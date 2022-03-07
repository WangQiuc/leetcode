__author_ = "wangqc"
# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        ctr = collections.Counter(x for i,x in enumerate(nums[1:]) if nums[i] == key)
        return max(ctr,key=lambda x:ctr[x])

if __name__ == "__main__":
    sol = Solution().mostFrequent

    print(sol(
        nums = [1,100,200,1,100], key = 1
    ))

    print(sol(
        nums = [2,2,2,2,3], key = 2
    ))