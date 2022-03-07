import string
from typing import List

__author_ = "wangqc"
import os

import collections, heapq, bisect, math, re
from utils import Utils
import functools, itertools
import random, sys


class Solution:
    def utf16decode(self, s):
        hs, t = "", ""
        for c in s:
            h = f"{ord(c):04x}"
            print(c, h)
            a, b = h[:2], h[2:]
            h = b + a
            x = (chr(int(b, 16))) + (chr(int(a, 16)))
            hs += h
            t += x
        return t, hs

    def base64decode(self, s):
        d = {'+':62, '-':63}
        for i, c in enumerate(string.ascii_uppercase):
            d[c] = i
        for i, c in enumerate(string.ascii_lowercase,26):
            d[c] = i
        for i in range(10):
            d[str(i)] = i+52
        t = "".join(f"{d[c]:06b}" for c in s)
        p = " ".join(t[i:i+8] for i in range(0,len(t),8))
        q = " ".join(f"{int(t[i:i+8],2):02x}" for i in range(0,len(t),8))
        return q



if __name__ == "__main__":

    sol = Solution().base64decode

    print(sol(
        s = "+w8XgXB9tBJDefCW9kAr3oDNbXpp9uvTvvGiyAxPujdsIPQ"
              ))

    # print(sol(
    #     s = "䝉浖杁湥㩴䤺噇䅭瑴獥㩴䠠呔⁐硥散瑰潩⁮湥潣湵整敲⹤圠湩瑈灴敒散癩剥獥潰獮㩥ㄠ〲㈰›桔⁥灯牥瑡潩⁮楴敭⁤畯൴⸊"
    #           ))
    # print(sol(
    #     s = "䝉浖杁湥㩴䤺噇䅭瑴獥㩴䠠呔⁐硥散瑰潩⁮湥潣湵整敲⹤圠湩瑈灴敓摮敒畱獥㩴ㄠ〲㈰›桔⁥灯牥瑡潩⁮楴敭⁤畯൴⸊"
    #           ))





