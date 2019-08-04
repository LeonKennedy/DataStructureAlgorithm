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
        import re
        ret = re.search('^(([+|-]\d+)|\d+)', str.strip())
        if ret:
            ret = ret.group()
            ret_int = int(ret)
        else:
            ret_int = 0
        if ret_int > 2147483647:
            ret_int = 2147483647
        elif ret_int < -2147483648:
            ret_int = -2147483648
        return ret_int

                
              

if __name__ == "__main__":
  s = Solution()
  string = '    -234 efji 123'
  assert -234 == s.myAtoi(string)
  string = "words and 987"
  assert 0 == s.myAtoi(string)
  string = '-91283472332'
  assert -2147483648 == s.myAtoi(string)
  string = '3.141592'
  assert 3 == s.myAtoi(string)
  string = ''
  assert 0 == s.myAtoi(string)
  string = '-'
  assert 0 == s.myAtoi(string)
  string = "+-2"
  assert 0 == s.myAtoi(string)
  # print(s.myAtoi(string))

