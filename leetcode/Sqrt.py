#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: Sqrt.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-07-26 12:08
# @Last Modified: 2019-07-26 12:08


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        left, right = 1, x
        while left < right:
            mid = left + (right - left) // 2
            if mid == x/mid:
                return mid
            elif mid > x/mid:
                right = mid - 1
            elif mid < x / mid:
                left = mid + 1
                if left > x /left:
                    return mid
        return left


if __name__ == '__main__':
    s = Solution()
    assert s.mySqrt(0) == 0
    fixtures = [[(4,9), 2], ((1,4), 1), ((4,9),2), ((9,16), 3)]
    for ran, val in fixtures:
        for i in range(*ran):
            assert s.mySqrt(i) == val
