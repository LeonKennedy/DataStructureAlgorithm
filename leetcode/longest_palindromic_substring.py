#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: longest_palindromic_substring.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 最长回文子序列
#               Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#               最优解使用了manacher算法 是朴素查询的优化
# @Create: 2018-09-06 16:11:10
# @Last Modified: 2018-09-06 16:11:10

import pdb, math

class Solution:

  def init(self, s):
    new_string = '$#'
    for char in s:
      new_string += char
      new_string += '#'
    return new_string + '%'

  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) <= 1:
      return s
    new_string = self.init(s)
    mx = 0
    mid = 0
    p = [0] * len(new_string)
    max_len = 0
    max_string = list()

    for i, char in enumerate(new_string):
      if char == '$' or char == '%':
        continue
      if (i < mx):
        p[i] = min(p[2 * mid - i], mx - i)
      else:
        p[i] = 1

      while (new_string[i - p[i]] == new_string[i + p[i]]):
        p[i] += 1
      if (mx < i + p[i]):
        mid = i
        mx = i + p[i]

      if p[i] - 1 > max_len:
        max_len = max(max_len, p[i] - 1)
        max_string = [ c for c in new_string[mid-max_len:mx] if not c == '#']

    return ''.join(max_string)

if __name__ == "__main__":
  so = Solution()
  s = 'abcbabcba'
  s = 'babad'
  print(so.longestPalindrome(s))




