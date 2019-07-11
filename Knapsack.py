#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: Knapsack.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 0-1 背包问题
# @Create: 2019-07-10 22:48
# @Last Modified: 2019-07-10 22:48

from copy import copy
from typing import List

class Knapsack:

    def __init__(self):
        self.maxW = 9
        self.items = [2, 2, 4, 6, 3]
        self.values = [3, 4, 8, 9, 6]
        print(f"item weight: {self.items}")

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
                yield from self.backtracking(i + 1, sub_bag)

    def dynamic(self):

        states = [-1] * (self.maxW + 1)
        states[0] = 0
        n = len(states)
        for i, item in enumerate(self.items):
            for j in range(n-1, -1, -1):  # 这里的倒叙是关键， 不然会覆盖之后的值
                if states[j] >= 0 and j + item < n and states[j + item] < states[j] + self.values[i]:
                    states[j + item] = self.values[i] + states[j]
        return states

    def find_combine(self, states) -> List:
        # 打印组合
        max_value = max(states)
        max_weight = states.index(max_value)
        print(f"max value: {max_value}    max weight: {max_weight}")
        output = list()
        for i, item in enumerate(self.items):
            if states[max_weight - item] == max_value - self.values[i]:
                output.append(i)
                max_value -= self.values[i]
                max_weight -= item
        return output


if __name__ == "__main__":
    k = Knapsack()
    max_bag = []
    print('---- backtracking --- ')
    for bag in k.backtracking(0, []):
        if sum(bag) > sum(max_bag):
            max_bag = bag
    print(max_bag)
    print('---- dynamic --- ')
    states = k.dynamic()
    output = k.find_combine(states)
    print(output)