__author_ = "wangqc"
# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

import os
import collections, sortedcontainers, heapq, bisect, math, re
from tkinter import N
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        s = set((i,j) for i, j in dig)
        return sum(all((i,j) in s for i in range(r1,r2+1) for j in range(c1,c2+1)) for r1,c1,r2,c2 in artifacts)

if __name__ == "__main__":
    sol = Solution().digArtifacts

    print(sol(
        n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]
    ))

    print(sol(
        n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]]
    ))
