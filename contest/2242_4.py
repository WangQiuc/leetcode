__author_ = "wangqc"
# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        g = collections.defaultdict(list)
        for x, y in edges:
            g[x].append((scores[y], y))
            g[y].append((scores[x], x))
        for x in range(n):
            g[x] = heapq.nlargest(3, g[x])
        ans = -1
        for x, y in edges:
            for wi, i in g[x]:
                if i != y:
                    for wj, j in g[y]:
                        if j != x and j != i:
                            ans = max(ans, wi+wj+scores[x]+scores[y])
        return ans

if __name__ == "__main__":
    sol = Solution().maximumScore

    print(sol(
        scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
    ))

    print(sol(
        scores = [9,20,6,4,11,12], edges = [[0,3],[5,3],[2,4],[1,3]]
    ))
