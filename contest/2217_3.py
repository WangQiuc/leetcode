__author_ = "wangqc"
# https://leetcode.com/problems/find-palindrome-with-fixed-length/

import os
import collections, sortedcontainers, heapq, bisect, math, re
from tkinter import N
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def kthPalindrome(self, queries: List[int], n: int) -> List[int]:
        def query(x):
            base = 10**(n-1>>1)
            if x > base*9:
                return -1
            x = base + x - 1
            # rx: front half of x string, remove middle digit if n is odd
            fx = x // 10 if n&1 else x
            while fx:
                x = x*10 + fx%10
                fx //= 10
            return x
        return [query(x) for x in queries]


if __name__ == "__main__":
    sol = Solution().kthPalindrome

    print(sol(
        queries = [1,2,3,4,5,90,91], n = 3
    ))

    print(sol(
        queries = [2,4,6], n = 4
    ))
