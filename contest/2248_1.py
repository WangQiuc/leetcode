__author_ = "wangqc"
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/submissions/

from ast import operator
import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted(set.intersection(*map(set,nums)))

if __name__ == "__main__":
    sol = Solution().intersection
    print(sol(
            nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
        ))

    print(sol(
            nums = [[1,2,3],[4,5,6]]
        ))