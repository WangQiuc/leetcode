__author_ = "wangqc"
# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

import os
import collections, sortedcontainers, heapq, bisect, math, re
from tkinter import N
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    # before deletion, if x in even idx, one x will be kept and next x is in odd idx
    # otherwise, x in odd idx, two x will be kept and next x is in odd idx as well
    def minDeletion(self, nums: List[int]) -> int:
        cnt, px = 0, -1
        # for even idx, px is previous x, for odd idx, px is -1
        for x in nums:
            if x == px:
                cnt += 1
            else:
                # after deletion, next x always in odd idx, px will be set to -1
                px = x if px < 0 else -1
        return cnt + (px >= 0)


if __name__ == "__main__":
    sol = Solution().minDeletion

    print(sol(
        nums = [1,1,2,3,5]
    ))

    print(sol(
        nums = [1,1,2,2,3,3]
    ))
