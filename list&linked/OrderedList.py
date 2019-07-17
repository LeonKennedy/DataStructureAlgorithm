#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: OrderedList.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description:
# 1. 实现一个大小固定的有序数组，支持动态增删改操作
# 2. 实现两个有序数组合并为一个有序数组
# @Create: 2019-07-17 12:19
# @Last Modified: 2019-07-17 12:19

from collections import UserList
from typing import List, TypeVar


_T = TypeVar('_T')


class OrderedList(UserList):

    def __init__(self, data: List, descending=False):
        self.descending = descending
        super(OrderedList, self).__init__(sorted(data, reverse=descending))

    def append(self, item: _T) -> None:
        p = len(self.data) - 1
        flag = (self.descending is False and self.data[p] > item) or (self.descending and self.data[p] < item)
        if flag:
            self.data.append(self.data[p])
        else:
            self.data.append(item)
            return
        while p >= 1:
            if (self.descending is False and self.data[p-1] > item) or (self.descending and self.data[p-1] < item):
                self.data[p] = self.data[p - 1]
                p -= 1
            else:
                self.data[p] = item
                return
        self.data[0] = item

    def __setitem__(self, key, item):
        del self.data[key]
        self.append(item)

    def __add__(self, other):
        return OrderedList([*self.data, *other.data])


if __name__ == "__main__":
    l = OrderedList([4, 9, 0,1,2,3])
    l.append(7)
    print(l)
    l = OrderedList([4, 9, 0, 1, 2, 3], True)
    l.append(7)
    print(l)
    l[2] = -1
    print(l)
    l2 = OrderedList([5,8,10,12,7])
    print(l+l2)