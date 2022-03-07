__author_ = "wangqc"
# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils


class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        ans = 0
        s = list(s)
        while s:
            i = s.index(s[-1])
            if i == len(s)-1:
                ans += i>>1
            else:
                ans += i
                s.pop(i)
            s.pop()
        return ans

if __name__ == "__main__":
    sol = Solution().minMovesToMakePalindrome

    print(sol(
        s = "aabb"
    ))

    print(sol(
        s = "letelt"
    ))