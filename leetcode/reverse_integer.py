#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: reverse_integer.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 7. Reverse Integer
#               Given a 32-bit signed integer, reverse digits of an integer.
# @Create: 2018-09-08 18:36:05
# @Last Modified: 2018-09-08 18:36:05
#

import pdb

class Solution:
  def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x > pow(2,31) - 1 or x < -2**31:
      return 0
    nums = list()
    print(x)
    while x > 0:
      pop = x % 10
      x //= 10
      nums.append(pop)
    reverse_num = 0
    nums.reverse()
    while len(nums) > 0:
      reverse_num  =  reverse_num * 10 + nums.pop()
    print(reverse_num)
    return nums

if __name__ == "__main__":
  s = Solution()
  s.reverse(123)

