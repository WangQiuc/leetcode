__author_ = "wangqc"
# https://leetcode.com/problems/find-the-difference-of-two-arrays/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1-s2), list(s2-s1)]

if __name__ == "__main__":
    sol = Solution().findDifference

    print(sol(
        nums1 = [1,2,3], nums2 = [2,4,6]
    ))

    print(sol(
        nums1 = [1,2,3,3], nums2 = [1,1,2,2]
    ))
