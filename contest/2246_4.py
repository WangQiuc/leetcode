__author_ = "wangqc"
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/submissions/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        T = [[] for i in range(len(s))]
        for i, p in enumerate(parent[1:],1):
            T[p].append(i)
        self.ans = 0
        def dfs(x):
            pq = [0,0]
            for y in T[x]:
                d = dfs(y)
                if s[x] != s[y]:
                    pq.append(d)
            pq = heapq.nlargest(2,pq)
            self.ans = max(self.ans, pq[0]+pq[1]+1)
            return max(pq)+1
        dfs(0)
        return self.ans

if __name__ == "__main__":
    sol = Solution().longestPath

    print(sol(
        parent = [-1,0,0,1,1,2], s = "abacbe"
    ))

    print(sol(
        parent = [-1,0,0,0], s = "aabc"
    ))

    print(sol(
        parent = [-1,0,1], s = "aab"
    ))