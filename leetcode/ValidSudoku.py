#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: ValidSudoku.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-08-09 17:51
# @Last Modified: 2019-08-09 17:51

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c, j), (i, c), (i // 3, j // 3, c)]
        return len(seen) == len(set(seen))

