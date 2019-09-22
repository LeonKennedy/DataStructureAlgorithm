#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: ZigZagConversion.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-09-22 18:29
# @Last Modified: 2019-09-22 18:29

import array


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        buckets = [array.array('u') for _ in range(numRows)]
        cell_size = (numRows - 1) << 1
        for index, v in enumerate(s):
            new_index = self.convert_index(index, cell_size, numRows)
            buckets[new_index].append(v)
        return ''.join(cell.tounicode() for cell in buckets)

    def convert_index(self, index: int, cell_size: int, num_rows: int):
        rest = index % cell_size
        flag, sub_rest = divmod(rest, num_rows)
        return num_rows - 2 - sub_rest if flag else sub_rest


def test():
    solution = Solution()
    assert "PINALSIGYAHRPI" == solution.convert("PAYPALISHIRING", 4)
    assert "PAHNAPLSIIGYIR" == solution.convert("PAYPALISHIRING", 3)
    assert "PYAIHRNAPLSIIG" == solution.convert("PAYPALISHIRING", 2)
    assert "PAYPALISHIRING" == solution.convert("PAYPALISHIRING", 1)


if __name__ == '__main__':
    test()
