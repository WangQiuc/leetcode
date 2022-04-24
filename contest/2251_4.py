__author_ = "wangqc"
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/submissions/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        A = collections.Counter()
        for l, r in flowers:
            A[l] += 1
            A[r+1] -= 1
        B = [(0,0)]
        agg = 0
        for x in sorted(A):
            B.append((x,agg:=agg+A[x]))
        return [B[bisect.bisect_left(B,(x+1,))-1][1] for x in persons]

if __name__ == "__main__":
    sol = Solution().fullBloomFlowers
    print(sol(
            flowers = [[1,6],[3,7],[9,12],[4,13]], persons = [2,3,7,11]
        ))

    print(sol(
            flowers = [[1,10],[3,3]], persons = [3,3,2]
        ))