#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: NumberofIslands.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-08-09 15:00
# @Last Modified: 2019-08-09 15:00

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_i = len(grid)
        if max_i == 0:
            return 0
        max_j = len(grid[0])
        all = set([(i,j) for i,row in enumerate(grid) for j, val in enumerate(row) if val == '1'])
        count = 0
        while len(all):
            island = set()
            count += 1
            a = all.pop()
            annulus = set()
            annulus.add(a)
            island.add(a)
            next_annulus = set()
            while len(annulus):
                for s in annulus:
                    for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ii, jj = s[0] + i, s[1] + j
                        if ii < 0 or ii >=max_i or jj < 0 or jj >= max_j:
                            continue
                        if grid[ii][jj] == '1' and (ii, jj) not in island:
                            next_annulus.add((ii, jj))
                island |= next_annulus
                annulus, next_annulus = next_annulus, set()
            all.difference_update(island)
        return count

    def numIslands2(self, grid):
        """ 更简介
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1))
                return 1
            return 0

        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

if __name__ == '__main__':
    s = Solution()
    d = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    assert s.numIslands(d) == 1
    d = [["1"]]
    assert s.numIslands(d) == 1
    d = [["1"], ["1"]]
    assert s.numIslands(d) == 1
    d = [["1", "0"]]
    assert s.numIslands(d) == 1
    d = []
    assert s.numIslands(d) == 0
    d = [["1","1","1"],["0","1","0"],["1","1","1"]]
    assert s.numIslands(d) == 1