#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: nqueue.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 51. N-Queens
#   The n-queens puzzle is the problem of
#   placing n queens on an n×n chessboard
#   such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space respectively.
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# @Create: 2019-07-10 11:00
# @Last Modified: 2019-07-10 11:00

from typing import List
from array import array
import copy


class NQueue:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chessboard = [array('u', '.' * n) for i in range(n)]
        output = list()
        for complete_chessboard in self.assign(chessboard, 0):
            solution = list()
            for row in complete_chessboard:
                solution.append(''.join(['Q' if i == 'Q' else '.' for i in row]))
            output.append(solution)
        return output

    def totalNQueens(self, n: int) -> int:
        chessboard = [array('u', '.' * n) for i in range(n)]
        num = 0
        for complete_chessboard in self.assign(chessboard, 0):
            num += 1
        return num

    def assign(self, chessboard: List[List[str]], layer: int) -> List[List[str]]:
        for column, cell in enumerate(chessboard[layer]):
            if cell != '.':
                continue
            sub_chessboard = copy.deepcopy(chessboard)
            sub_chessboard[layer][column] = 'Q'
            if layer == len(chessboard) - 1:
                yield sub_chessboard
            else:
                self.fill(sub_chessboard, layer, column)
                for output in self.assign(sub_chessboard, layer+1):
                    yield output

    def fill(self, chessboard, layer, column):
        for row in chessboard:
            row[column] = '+'
        chessboard[layer][column] = 'Q'
        length = len(chessboard)
        i = layer + 1
        while i < length:
            left = column - i + layer
            if left >= 0:
                chessboard[i][left] = '+'
            right = column + i - layer
            if right < length:
                chessboard[i][right] = '+'
            i += 1

if __name__ == "__main__":
    q = NQueue()
    print(q.solveNQueens(4))