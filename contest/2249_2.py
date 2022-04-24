__author_ = "wangqc"
# https://leetcode.com/problems/count-lattice-points-inside-a-circle/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        s = set()
        for x, y, r in circles:
            for dx in range(-r,r+1):
                mxdy = int((r*r-dx*dx)**0.5)
                for dy in range(-mxdy,mxdy+1):
                    s.add((x+dx,y+dy))
        return len(s)

if __name__ == "__main__":
    sol = Solution().countLatticePoints
    print(sol(
            circles = [[2,2,1]]
        ))

    print(sol(
            circles = [[2,2,2],[3,4,1]]
        ))