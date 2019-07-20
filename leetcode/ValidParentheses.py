#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: ValidParentheses.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 有效括号
# https://leetcode.com/problems/valid-parentheses/
# @Create: 2019-07-21 00:14
# @Last Modified: 2019-07-21 00:14


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        matcher = {('[',']'), ('{','}'), ('(',')')}
        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            else:
                try:
                    left = stack.pop()
                except IndexError:
                    return False
                if (left, i) in matcher:
                    continue
                else:
                    return False
        return True if len(stack) == 0 else False