__author_ = "wangqc"
# https://leetcode.com/problems/design-an-atm-machine/

import os
import collections, sortedcontainers, heapq, bisect, math, re
import functools, itertools
import random, sys
from typing import List

from utils import Utils

class ATM:

    def __init__(self):
        self.notes = (20,50,100,200,500)
        self.ctr = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        self.ctr = [x+y for x,y in zip(self.ctr, banknotesCount)]

    def withdraw(self, amount: int) -> List[int]:
        wallet = [0] * 5
        for i in range(4,-1,-1):
            k = min(self.ctr[i], amount//self.notes[i])
            wallet[i] += k
            amount -= k*self.notes[i]
        if amount:
            return [-1]
        self.deposit([-x for x in wallet])
        return wallet

if __name__ == "__main__":
    atm = ATM()
    print(atm.deposit([0,0,1,2,1]))
    print(atm.withdraw(600))
    print(atm.deposit([0,1,0,1,1]))
    print(atm.withdraw(600))
    print(atm.withdraw(550))