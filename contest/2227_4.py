__author_ = "wangqc"
# https://leetcode.com/problems/encrypt-and-decrypt-strings/

import os
import collections, sortedcontainers, heapq, bisect, math, re
from tkinter import N
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.e = {k : v for k, v in zip(keys, values)}
        self.d = collections.Counter(map(self.encrypt, dictionary))

    def encrypt(self, word1: str) -> str:
        return "".join(self.e[c] for c in word1)

    def decrypt(self, word2: str) -> int:
        return self.d[word2]

if __name__ == "__main__":
    keys = ['a', 'b', 'c', 'd']
    values = ["ei", "zf", "ei", "am"]
    dictionary = ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]


    sol = Encrypter(keys, values, dictionary)

    print(sol.encrypt(
        word1 = "abcd"
    ))

    print(sol.decrypt(
        word2 = "eizfeiam"
    ))
