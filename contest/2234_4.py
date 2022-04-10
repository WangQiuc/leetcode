__author_ = "wangqc"
# https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        a = sorted(x for x in flowers if x < target)
        n = len(a)
        f, k = len(flowers) - n, newFlowers
        ans = f * full
        if not a:
            return ans
        # b[i]: total flower# to fill all a[:i+1] upto a[i+1]
        b = [i*a[i]-s for i,s in enumerate(itertools.accumulate(a[:-1]),1)] + [0] # add pivot

        # k flowers are allocated to increment min flower# among a[:n]
        def get_min(k,n):
            i = bisect.bisect(b,k,lo=0,hi=n)
            return min(a[i] + (k-b[i-1])//(i+1), target-1) # k-b[i-1] leftover shared with i+1 slots

        ans += max((k>=target*n-sum(a))*n * full, get_min(k,n-1) * partial)  # two corners
        for i,x in enumerate(a[:0:-1],1):
            if k < target-x:
                break
            k -= target-x
            ans = max(ans, (f+i) * full + get_min(k,n-i-1) * partial)
        return ans

if __name__ == "__main__":
    sol = Solution().maximumBeauty

    print(sol(
        flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1
    ))

    print(sol(
        flowers = [2,4,5,3], newFlowers = 10, target = 5, full = 2, partial = 6
    ))

    print(sol(
        flowers = [1,1], newFlowers = 2, target = 2, full = 1, partial = 2
    ))

    print(sol(
        flowers = [5,5,15,1,9], newFlowers = 36, target = 12, full = 9, partial = 2
    ))

    print(sol(
        flowers = [8,2], newFlowers = 24, target = 18, full = 6, partial = 3
    ))

    print(sol(
        flowers = [10,9,16,14,6,5,11,12,17,2,11,15,1], newFlowers = 80, target = 14, full = 15, partial = 1
    ))
