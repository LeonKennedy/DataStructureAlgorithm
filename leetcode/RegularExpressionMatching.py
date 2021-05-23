#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: RegularExpressionMatching.py
@time: 2021/5/23 10:11 上午
@desc: 正则表达式匹配
"""
from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        fsm = FiniteStateMachine(p)
        return fsm.trans(s, 0, 0)


class FiniteStateMachine:
    def __init__(self, re):
        self.queue = self.create_regular(re)

    def create_regular(self, re):
        q = []
        for i in re:
            if i == '*':
                q[-1].star = True
            else:
                q.append(Cell(i))
        qq = []
        for i in q:
            if qq and qq[-1] == i:
                continue
            else:
                qq.append(i)
        return qq

    @lru_cache
    def trans(self, s, i, j) -> bool:
        if j >= len(self.queue):
            return True if i >= len(s) else False
        else:
            cell = self.queue[j]
            if cell.match(s[i:]):
                if cell.star:
                    return self.trans(s, i + cell.size, j + 1) or self.trans(s, i + cell.size, j) or self.trans(s, i,
                                                                                                                j + 1)
                else:
                    return self.trans(s, i + cell.size, j + 1)
            else:
                if cell.star:
                    return self.trans(s, i, j + 1)
                else:
                    return False


class Cell:
    def __init__(self, c: str, star=False):
        self.star = star
        self.size = len(c)
        self._matcher = c

    def __repr__(self) -> str:
        return self._matcher + '*' if self.star else self._matcher

    def __eq__(self, other) -> bool:
        if self.star:
            return self._matcher == other._matcher and self.star == other.star
        else:
            return False

    def match(self, s: str) -> bool:
        if len(s) == 0:
            return False
        if self._matcher == '.':
            return True
        else:
            return s.startswith(self._matcher)


if __name__ == '__main__':
    # res = ['a*', 'a.*', "aaa*", "a*a*", "aaa.*"]
    # for re in res:
    #     fsm = FiniteStateMachine(re)
    #     print(fsm.queue)
    ss = Solution()
    test_unit = [
        ["aa", "aa", True],
        ["aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c", False],
        ["bbbba", ".*a*a", True],
        ["aa", "a", False],
        ["aa", "a*", True],
        ["ab", ".*", True],
        ["aab", "c*a*b", True],
        ["mississippi", "mis*is*p*.", False],
        ["aaa", "a.a", True],
        ["a", "ab*", True],
        ["ab", ".*c", False],
    ]
    for s, p, ass in test_unit:
        if ss.isMatch(s, p) == ass:
            print(s, p, "pass")
        else:
            print(s, p, 'error')
