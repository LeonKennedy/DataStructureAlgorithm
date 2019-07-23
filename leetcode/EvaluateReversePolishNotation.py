#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: EvaluateReversePolishNotation.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description:
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# @Create: 2019-07-21 16:23
# @Last Modified: 2019-07-21 16:23
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for s in tokens:
            if s == '+':
                e = stack.pop() + stack.pop()
                stack.append(e)
            elif s == '-':
                r = stack.pop()
                e = stack.pop() - r
                stack.append(e)
            elif s == '*':
                e = stack.pop() * stack.pop()
                stack.append(e)
            elif s == '/':
                r = stack.pop()
                e = int(stack.pop()/r)
                stack.append(e)
            else:
                stack.append(int(s))
        return stack.pop()

if __name__ == "__main__":
    s = Solution()
    s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])

