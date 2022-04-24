__author_ = "wangqc"
# https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        X, Y = zip(*sorted(rectangles))
        A = [collections.Counter(Y)]
        for y in Y:
            A.append(A[-1].copy())
            A[-1][y] -= 1
        count = lambda x,y: sum(v for k, v in A[bisect.bisect(X,x-1)].items() if k >= y)
        return [count(x,y) for x,y in points]

if __name__ == "__main__":
    sol = Solution().countRectangles
    print(sol(
            rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]
        ))

    print(sol(
            rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]
        ))