#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: StringMatcher.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-06-24 20:29
# @Last Modified: 2019-06-24 20:29


class StringMatch:
    pass


class BoyerMoore:

    def __init__(self, matcher):
        self._matcher = matcher
        self._l = len(self._matcher)

    def search(self, main) -> int:
        return self._check(main, 0)

    def _check(self, main, pass_length) -> int:
        mp = len(self._matcher) - 1
        p = pass_length + mp
        i = p
        while self._matcher[mp] == main[i]:
            if mp == 0:
                return i
            mp -= 1
            i -= 1
        good_move = self._good(main[i+1:p+1], mp)
        bad_move = self._bad(main, i, mp)
        best_move = max(good_move, bad_move)
        return self._check(main, pass_length+best_move)

    def _bad(self, main, p, mp) -> int:
        mi = mp - 1
        while self._matcher[mi] != main[p] and mi >= 0:
            mi -= 1
        return mp - mi

    def _good(self, good_string, mp):
        if good_string == '':
            return 0
        try:
            last_index = self._matcher[0:mp+1].index(good_string)
        except ValueError:
            return -1
        return last_index - mp


if __name__ == "__main__":
    bm = BoyerMoore('bcad')
    index = bm.search('abcdbcad')
    print(index)