__author_ = "wangqc"
# https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # R[i][j+1] (number of factor 2, number of factor 5) in grid[i][:j]
        R, C = [[(0,0)] for _ in range(m)], [[(0,0)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                x, p2, p5 = grid[i][j], 0, 0
                while x and x&1 == 0:
                    x >>= 1
                    p2 += 1
                while x and x%5 == 0:
                    x //= 5
                    p5 += 1
                R[i].append((R[i][-1][0]+p2, R[i][-1][1]+p5))
                C[j].append((C[j][-1][0]+p2, C[j][-1][1]+p5))
        def get_val(i, j):
            r1, r2 = R[i][j+1], (R[i][n][0]-R[i][j][0], R[i][n][1]-R[i][j][1])
            c1, c2 = C[j][i], (C[j][m][0]-C[j][i+1][0], C[j][m][1]-C[j][i+1][1])
            return max(min(r[0]+c[0],r[1]+c[1]) for r in (r1,r2) for c in (c1,c2))
        return max(get_val(i,j) for i in range(m) for j in range(n))

if __name__ == "__main__":
    sol = Solution().maxTrailingZeros

    print(sol(
        grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
    ))

    print(sol(
        grid = [[4,3,2],[7,6,1],[8,8,8]]
    ))

    print(sol(
        grid = [[1,5,2,4,25]]
    ))