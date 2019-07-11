#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: Knapsack.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 0-1 背包问题
# @Create: 2019-07-10 22:48
# @Last Modified: 2019-07-10 22:48

from copy import copy
class Knapsack:

    def __init__(self):
        self.maxW = 9
        self.items = [2,2,4,6,3]
        self.values = []

    def backtracking(self, i, bag):
        if i >= len(self.items):
            yield bag
        else:
            negative_bag = copy(bag)
            yield from self.backtracking(i + 1, negative_bag)
            if sum(bag) + self.items[i] > self.maxW:
                yield bag
            else:
                sub_bag = copy(bag)
                sub_bag.append(self.items[i])
                yield from self.backtracking(i+1, sub_bag)


if __name__ == "__main__":
    k = Knapsack()
    max_bag = []
    for bag in k.backtracking(0, []):
        print(bag)
        if sum(bag) > sum(max_bag):
            max_bag = bag
    print(max_bag)