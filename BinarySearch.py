#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: BinarySearch.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 二分查找
# @Create: 2019-06-15 11:11
# @Last Modified: 2019-06-15 11:11

from typing import Any
import numpy as np


def is_exist(needle, haystack: Any):
    if len(haystack) == 0:
        return False
    return binary_search(haystack, 0, len(haystack) - 1, needle) > -1


def find_index(needle, haystack, first=True):
    """
    + 查找第一个给定值的元素
    :param needle:
    :param haystack:
    :return:
    """
    mid = binary_search(haystack, 0, len(haystack) - 1, needle)
    other = mid
    while True:
        if first:
            tmp = binary_search(haystack, 0, other - 1, needle)
        else:
            tmp = binary_search(haystack, other+1, len(haystack)-1, needle)
        if tmp == -1:
            return other
        else:
            other = tmp


def first_gt_item(needle, haystack):
    """
    + 查找第一个大于给定值的元素
    :param needle:
    :param haystack:
    :return: index of haystack: int
    """
    last = find_index(needle, haystack, False)
    if last > len(haystack) - 1:
        return last
    else:
        return last+1


def last_ge_item(needle, haystack):
    """
    + 查找最后一个小于等于给定值的元素
    :param needle:
    :param haystack:
    :return:
    """
    return binary_search_close(haystack, 0, len(haystack)-1, needle)


def close_item(self, item):
    pass


def binary_search(data, l, r, item):
    if r < l:
        return -1
    mid = (l + r) >> 1
    if data[mid] == item:
        return mid
    elif data[mid] < item:
        return binary_search(data, mid + 1, r, item)
    else:
        return binary_search(data, l, mid - 1, item)


def binary_search_close(data, l, r, item):
    if r < 0:
        return None
    if r < l:
        return r
    mid = (l+r) >> 1
    if data[mid] > item:
        return binary_search_close(data, l, mid-1, item)
    else:
        return binary_search_close(data, mid+1, r, item)


def test():
    a = [1]
    assert(is_exist(1, a))
    assert(is_exist(0, a) == False)
    assert(last_ge_item(0, a) == None)
    assert(last_ge_item(1, a) == 0)

    a = [1, 2]
    assert (is_exist(1, a))
    assert (is_exist(2, a))
    assert (is_exist(0, a) == False)
    assert (is_exist(3, a) == False)
    assert(last_ge_item(0, a) == None)
    assert(last_ge_item(1, a) == 0)
    assert(last_ge_item(1.5, a) == 0)
    assert(last_ge_item(2, a) == 1)
    assert(last_ge_item(3, a) == 1)

    a = [1, 1, 2, 2]
    assert (is_exist(1, a))
    assert (is_exist(2, a))
    assert (is_exist(0, a) == False)
    assert (is_exist(3, a) == False)
    assert (find_index(2, a) == 2)
    assert (find_index(2, a, False) == 3)
    assert (find_index(1, a) == 0)
    assert (find_index(1, a, False) == 1)

    while True:
        a = np.random.randint(0, 100, 100)
        a.sort()
        print(a)
        item = 17
        if is_exist(item, a):
            print("fisrt index: \t", find_index(item, a))
            print("last index: \t",find_index(item, a, False))
            print("first great: \t", first_gt_item(item, a))
            print("last great or equal: \t", last_ge_item(item, a))
        else:

            print("last great or equal: \t", last_ge_item(item, a))
        break


if __name__ == "__main__":
    test()
