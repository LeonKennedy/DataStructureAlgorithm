#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: CountingSort.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description:  适用于K比较少的情况
# @Create: 2019-06-13 20:47
# @Last Modified: 2019-06-13 20:47
import array
import random


class CountingSort:

    def counting_sort(self, data, n):
        c = array.array('l', [0] * n)
        for d in data:
            c[d] += 1
        temp = 0
        for i in range(n):
            c[i] += temp
            temp = c[i]
        output = array.array('l', [20] * len(data))
        for d in data:
            index = c[d] - 1
            c[d] -= 1
            output[index] = d
        return output


def test():
    max = 20
    a = [random.randint(0, max - 1) for _ in range(100)]
    data = array.array('l', a)
    print(data)
    bs = CountingSort()
    data = bs.counting_sort(data, n=max)
    print(data)


if __name__ == "__main__":
    test()
