__author_ = "wangqc"
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

import os
import collections, sortedcontainers, heapq, bisect, math, re
from tkinter import N, W
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        g, gr = collections.defaultdict(dict), collections.defaultdict(dict)
        for x, y, w in edges:
            g[x][y] = gr[y][x] = min(g[x].get(y,w), w)

        def dijkstra(g, s):
            d = [math.inf] * n
            d[s] = 0
            pq = [(0,s)]
            while pq:
                w, x = heapq.heappop(pq)
                if w != d[x]:
                    continue
                for y, dw in g[x].items():
                    if d[y] > dw+w:
                        d[y] = dw+w
                        heapq.heappush(pq,(d[y],y))
            return d

        d1, d2, d3 = dijkstra(g,src1), dijkstra(g,src2), dijkstra(gr,dest)
        ans = min(d1[i]+d2[i]+d3[i] for i in range(n))
        return -1 if ans == math.inf else ans


if __name__ == "__main__":
    sol = Solution().minimumWeight

    print(sol(
        n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5
    ))

    print(sol(
        n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2
    ))

    print(sol(
        n = 8, edges = [[4,7,24],[1,3,30],[4,0,31],[1,2,31],[1,5,18],[1,6,19],[4,6,25],[5,6,32],[0,6,50]], src1 = 4, src2 = 1, dest = 6
    ))

    print(sol(
        n = 5, edges = [[4,2,20],[4,3,46],[0,1,15],[0,1,43],[0,1,32],[3,1,13]], src1 = 0, src2 = 4, dest = 1
    ))
