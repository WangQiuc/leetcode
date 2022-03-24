__author_ = "wangqc"
# https://leetcode.com/problems/range-sum-query-mutable/

import os
import collections, sortedcontainers, heapq, bisect, math, re
from tkinter import N
import functools, itertools
import random, sys
from typing import List

from utils import Utils

# Binary Index Tree, simple structure and less constant factor
class BIT:

    def __init__(self, n):
        self.B = [0] * n
        self.n = n

    def update(self, i, v):
        while i < self.n:
            self.B[i] += v
            i += i&-i

    def query(self, i):
        s = 0
        while i:
            s += self.B[i]
            i -= i&-i
        return s

class NumArrayBIT:

    def __init__(self, nums: List[int]):
        self.A = nums
        self.B = BIT(len(nums)+1)
        for i, x in enumerate(nums,1):
            self.B.update(i,x)

    def update(self, index: int, val: int) -> None:
        d = val - self.A[index]
        self.A[index] = val
        self.B.update(index+1, d)

    def sumRange(self, left: int, right: int) -> int:
        return self.B.query(right+1) - self.B.query(left)

# Segment Tree, easy to understand but complicant to implement
class Node:

    def __init__(self, lo, hi, val=0, left=None, right=None):
        self.lo = lo
        self.hi = hi
        self.val = val
        self.left = left
        self.right = right

class NumArraySegTree:

    def __init__(self, nums: List[int]):
        self.A = nums
        self.root = self.build(0, len(nums)-1)

    def build(self, lo, hi):
        if lo == hi:
            return Node(lo, hi, self.A[lo])
        mid = lo + hi >> 1
        node = Node(lo, hi, 0, self.build(lo, mid), self.build(mid+1, hi))
        node.val = node.left.val + node.right.val
        return node

    def update_node(self, index, val, node):
        if node.lo == node.hi:
            node.val = val
            return
        mid = node.lo + node.hi >> 1
        if index <= mid:
            self.update_node(index, val, node.left)
        else:
            self.update_node(index, val, node.right)
        node.val = node.left.val + node.right.val

    def sum_node_range(self, left, right, node):
        if left == node.lo and right == node.hi:
            return node.val
        mid = node.lo + node.hi >> 1
        if right <= mid:
            return self.sum_node_range(left, right, node.left)
        if left > mid:
            return self.sum_node_range(left, right, node.right)
        return self.sum_node_range(left, mid, node.left) + self.sum_node_range(mid+1, right, node.right)

    def update(self, index: int, val: int) -> None:
        return self.update_node(index, val, self.root)

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_node_range(left, right, self.root)


if __name__ == "__main__":
    numArray = NumArrayBIT([1, 3, 5])
    print(numArray.sumRange(0, 2))
    print(numArray.update(1, 2))
    print(numArray.sumRange(0, 2))

    numArray = NumArraySegTree([1, 3, 5])
    print(numArray.sumRange(0, 2))
    print(numArray.update(1, 2))
    print(numArray.sumRange(0, 2))