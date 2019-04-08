#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: longest_palindromic_substring.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 对角线遍历
#             Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in
#             diagonal order as shown in the below image.
# @Create: 2019-04-08 23:52:10
# @Last Modified: 2019-04-08 23:52:10
# score
# Runtime: 136 ms, faster than 54.50% of Python3 online submissions for Diagonal Traverse.
# Memory Usage: 15.4 MB, less than 10.42% of Python3 online submissions for Diagonal Traverse.
from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        i = 0
        j = 0
        output = [matrix[i][j]]
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        if (m + 1) * (n + 1) == 0:
            return []
        for t in range((m + 1) * (n + 1) - 1):
            if (i + j) % 2 == 0:  # up
                if j == n:
                    i += 1
                elif i == 0:
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:  # down
                if i == m:
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    i += 1
                    j -= 1
            output.append(matrix[i][j])
        return output


if __name__ == "__main__":
    s = Solution()
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    data = [
        [1, 2],
        [3, 4]
    ]
    out = s.findDiagonalOrder(data)
    print(out)
