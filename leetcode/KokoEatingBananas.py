#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: KokoEatingBananas.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-09-15 10:21
# @Last Modified: 2019-09-15 10:21
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l,r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if sum(math.ceil(i/m) for i in piles) > H:
                l = m+ 1
            else:
                r = m
        return l


if __name__ == '__main__':
    s = Solution()
    l = [332484035,
         524908576,
         855865114,
         632922376,
         222257295,
         690155293,
         112677673,
         679580077,
         337406589,
         290818316,
         877337160,
         901728858,
         679284947,
         688210097,
         692137887,
         718203285,
         629455728,
         941802184]
    h = 823855818
    print(s.minEatingSpeed(l, h))
