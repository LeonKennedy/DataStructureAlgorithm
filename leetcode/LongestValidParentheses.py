#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: LongestValidParentheses.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description:
# https://leetcode.com/problems/longest-valid-parentheses/
# @Create: 2019-07-21 00:27
# @Last Modified: 2019-07-21 00:27


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, res, s = [0], 0, ')' + s
        for i in range(1, len(s)):
            if s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
                res = max(res, i - stack[-1])
            else:
                stack.append(i)
        return res


if __name__ == "__main__":
    c = Solution()
    datas = ['()(()','((', ')', "()", '(()()', '((())']
    for data in datas:
        print(f"{data} : {c.longestValidParentheses(data)}")



