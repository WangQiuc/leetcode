__author_ = "wangqc"
# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return [f"{chr(c)}{r}"
            for c in range(ord(s[0]),ord(s[3])+1)
            for r in range(int(s[1]),int(s[4])+1)]

if __name__ == "__main__":
    sol = Solution().cellsInRange

    print(sol(
        s = "K1:L2"
    ))

    print(sol(
        s = "A1:F1"
    ))