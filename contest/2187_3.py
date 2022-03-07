__author_ = "wangqc"
# https://leetcode.com/problems/minimum-time-to-complete-trips/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo = min(time)
        return bisect.bisect_left(range(totalTrips*lo+1),totalTrips,lo,key=lambda x:sum(x//t for t in time))

        # lo = min(time)
        # hi = totalTrips*lo
        # while lo < hi:
        #     x = lo + hi >> 1
        #     if sum(x//t for t in time) >= totalTrips:
        #         hi = x
        #     else:
        #         lo = x+1
        # return lo

if __name__ == "__main__":
    sol = Solution().minimumTime

    print(sol(
        time = [1,2,3], totalTrips = 5
    ))

    print(sol(
        time = [2], totalTrips = 1
    ))