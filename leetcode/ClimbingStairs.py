#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: ClimbingStairs.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-07-23 11:58
# @Last Modified: 2019-07-23 11:58


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a = 1
        b = 2
        for i in range(n):
            b, a = a + b , b
        return b

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(10))
