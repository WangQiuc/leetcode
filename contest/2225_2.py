__author_ = "wangqc"
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        a = collections.Counter()
        s = set()
        for x, y in matches:
            s.add(x)
            s.add(y)
            a[y] += 1
        # output should be returned in increasing order, not a trouble for cpp set
        return [sorted(x for x in s if a[x] == d) for d in (0,1)]

if __name__ == "__main__":
    sol = Solution().findWinners

    print(sol(
        matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    ))

    print(sol(
        matches = [[2,3],[1,3],[5,4],[6,4]]
    ))
