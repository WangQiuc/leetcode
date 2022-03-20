__author_ = "wangqc"
# https://leetcode.com/problems/count-collisions-on-a-road/

import os
import collections, sortedcontainers, heapq, bisect, math, re
from tkinter import N
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def countCollisions(self, directions: str) -> int:
        s = directions.lstrip('L').rstrip('R')
        return len(s) - s.count('S')


if __name__ == "__main__":
    sol = Solution().countCollisions

    print(sol(
        directions = "RLRSLL"
    ))

    print(sol(
        directions = "LLRR"
    ))
