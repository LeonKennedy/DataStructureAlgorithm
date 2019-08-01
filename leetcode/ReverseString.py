#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: ReverseString.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-08-01 10:32
# @Last Modified: 2019-08-01 10:32

from typing import List



class Solution:


    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
