__author_ = "wangqc"
# https://leetcode.com/problems/sort-the-jumbled-numbers/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def f(x):
            if x < 10:
                return mapping[x]
            y, p = 0, 1
            while x:
                y += (mapping[x%10])*p
                x //= 10
                p *= 10
            return y
        return sorted(nums, key=f)



if __name__ == "__main__":
    sol = Solution().sortJumbled

    print(sol(
        mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]
    ))

    print(sol(
        mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123]
    ))