__author_ = "wangqc"
# https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def minimizeResult(self, expression: str) -> str:
        a, b = expression.split("+")
        mn = int(a) + int(b)
        ans = f"({expression})"
        for i in range(len(a)):
            a1, a2 = a[:i], a[i:]
            for j in range(1, len(b)+(i!=0)):
                b1, b2 = b[:j], b[j:]
                c = int(a2)+int(b1)
                if a1: c *= int(a1)
                if b2: c *= int(b2)
                if c < mn:
                    mn, ans = c, f"{a1}({a2}+{b1}){b2}"
        return ans

if __name__ == "__main__":
    sol = Solution().minimizeResult

    print(sol(
        expression = "247+38"
    ))

    print(sol(
        expression = "12+34"
    ))

    print(sol(
        expression = "999+999"
    ))

    print(sol(
        expression = "1+13"
    ))

    print(sol(
        expression = "13+1"
    ))
