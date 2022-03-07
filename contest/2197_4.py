__author_ = "wangqc"
# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            while ans and (g := math.gcd(x, ans[-1])) != 1:
                x *= ans.pop() // g
            ans.append(x)
        return ans

if __name__ == "__main__":
    sol = Solution().replaceNonCoprimes
    util = Utils()

    print(sol(
        nums = [6,4,3,2,7,6,2]
    ))

    print(sol(
        nums = [2,2,1,1,3,3,3]
    ))

    print(sol(
        nums = [2,5,4,6,8,3,10,7,6,77]
    ))