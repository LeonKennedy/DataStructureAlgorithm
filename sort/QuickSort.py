#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: QuickSort.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-06-11 20:47
# @Last Modified: 2019-06-11 20:47
import array
import random
from typing import List

class QuickSort:

    def quick_sort(self, data, p, r, ascending=True):
        if p >= r:
            return
        i = self.partition(data, p, r)
        self.quick_sort(data, p, i-1,  ascending)
        self.quick_sort(data, i+1, r, ascending)

    def partition(self, data: List, p: int, r: int) -> int:
        point = data[r]
        i = p
        j = r - 1
        while i < j:
            while data[i] <= point and i < r:
                i += 1
            while data[j] > point:
                j -= 1
            if i < j:
                data[i], data[j] = data[j], data[i]
        if data[i] > point:
            data[r], data[i] = data[i], point
        return i


def test():
    ms = QuickSort()
    a = [1, 2]
    ms.quick_sort(a, 0, len(a)-1)
    print(a)
    a = [2, 1]
    ms.quick_sort(a, 0, len(a)-1)
    print(a)

    a = [2, 1, 0]
    ms.quick_sort(a, 0, len(a)-1)
    print(a)
    a = [2, 1, 3]
    ms.quick_sort(a, 0, len(a)-1)
    print(a)
    a = array.array('l', [1, 7, 5, 0, 6, 9, 2, 4, 8, 3])
    ms.quick_sort(a, 0, len(a) - 1)
    print(a)

    data = list(range(20))
    random.shuffle(data)
    data = array.array('l', data)
    print(data)
    ms.quick_sort(data, 0, len(data) - 1)
    print(data)


if __name__ == "__main__":
    test()
