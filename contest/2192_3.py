__author_ = "wangqc"
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = collections.defaultdict(set)
        ans = [[] for _ in range(n)]
        for x, y in edges:
            g[x].add(y)
        def dfs(x,p):
            for y in g[x]:
                if not ans[y] or ans[y][-1] != p:
                    ans[y].append(p)
                    dfs(y,p)
        # in sorted order
        for i in range(n):
            dfs(i,i)
        return ans

    def getAncestorsTopo(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = collections.defaultdict(set)
        d = [set() for _ in range(n)]
        ctr = [0] * n
        for x, y in edges:
            g[x].add(y)
            d[y].add(x)
            ctr[y] += 1
        q = [x for x in range(n) if ctr[x] == 0]
        for x in q:
            for y in g[x]:
                d[y] |= d[x]
                ctr[y] -= 1
                if ctr[y] == 0:
                    q.append(y)
        return [sorted(s) for s in d]



if __name__ == "__main__":
    sol = Solution().getAncestors

    print(sol(
        n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
    ))

    print(sol(
        n = 5, edges = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    ))