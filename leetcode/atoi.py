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
        for c in str:
          if c == ' ':
            i += 1
          else:
            break
        if len(str[i:])  == 0:
          return 0
        if str[i] == '-':
            sign = -1
            i += 1
        elif str[i] == '+':
            sign = -1
            i += 1
        if len(str[i:])  == 0:
          return 0
        for c in str[i:]:
            if c >= '0' and c <= '9':
                out = out * 10 + int(c)
            else:
                break
        if out * sign > 2**31 - 1:
            return 2**31 -1
        if out * sign < -2**31:
            return -2**31
        return out * sign
                
              

if __name__ == "__main__":
  s = Solution()
  string = '    -234 efji 123'
  string = ' '
  string = ''
  string = '-'
  string = '+1'
  print(s.myAtoi(string))
  assert -234 == s.myAtoi(string)
