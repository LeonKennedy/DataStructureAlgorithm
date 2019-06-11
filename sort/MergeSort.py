#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: MergeSort.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-06-11 19:59
# @Last Modified: 2019-06-11 19:59

from typing import List
import random
import array

class MergeSort:

    def merge_sort(self, data: array, ascending=True) -> List:
        if len(data) == 1:
            return data
        mid = len(data) // 2
        return self.merge(self.merge_sort(data[:mid],  ascending), self.merge_sort(data[mid:], ascending), ascending)

    def merge(self, left, right, ascending):
        a = array.array('l')
        left_index = 0
        right_index = 0
        while len(left) > left_index and len(right) > right_index:
            if self.compare(left[left_index], right[right_index], ascending):
                a.append(left[left_index])
                left_index += 1
            else:
                a.append(right[right_index])
                right_index += 1

            if left_index == len(left):
                a.extend(right[right_index:])
                break
            if right_index == len(right):
                a.extend(left[left_index:])
                break
        return a

    def compare(self, left, right, ascending):
        if left <= right:
            return True if ascending else False
        else:
            return False if ascending else True


def test():
    data = list(range(20))
    random.shuffle(data)
    data = array.array('l', data)
    print(data)
    ms = MergeSort()
    data = ms.merge_sort(data, False)
    print(data)

if __name__ == "__main__":
    test()