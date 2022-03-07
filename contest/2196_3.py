__author_ = "wangqc"
# https://leetcode.com/problems/create-binary-tree-from-descriptions/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import TreeNode, Utils

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> [TreeNode]:
        d = {}
        c = set()
        for x, y, l in descriptions:
            nx, ny = d.setdefault(x, TreeNode(x)), d.setdefault(y, TreeNode(y))
            if l:
                nx.left = ny
            else:
                nx.right = ny
            c.add(y)
        return d[(set(d)-c).pop()]

if __name__ == "__main__":
    sol = Solution().createBinaryTree
    util = Utils()

    print(util.tree2list(sol(
        descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
    )))

    print(util.tree2list(sol(
        descriptions = [[1,2,1],[2,3,0],[3,4,1]]
    )))