#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: atoi.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description:  String to Integer (atoi)
# @Create: 2018-09-10 18:11:18
# @Last Modified: 2018-09-10 18:11:18
#

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        out = 0
        sign = 1
        i = 0
        while not (str[i] >= '0' and str[i] <= '9'):
            i += 1 
        if i>0 and str[i-1] == '-':
            sign = -1
        for c in str[i:]:
            if c >= '0' and c <= '9':
                out = out * 10 + int(c)
            else:
                return out * sign
        return out * sign
                
              

if __name__ == "__main__":
  s = Solution()
  string = ' -b   234 efji 123'
  print(s.myAtoi(string))
  assert 234 == s.myAtoi(string)