#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: knapsack.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-09-12 17:25
# @Last Modified: 2019-09-12 17:25
import random
from collections import Counter


class Bag:

    def solution(self, weights, values, bag_weight):
        table = Counter({0: 0})

        for i, weight in enumerate(weights):
            new_table = table.copy()
            for k, v in table.items():
                if k + weight <= bag_weight:
                    new_table[k + weight] = max(new_table[k + weight], v + values[i])
            table = new_table
        max_value = max_weight = 0
        for k, v in table.items():
            if v > max_value:
                max_value = v
                max_weight = k
        return max_value, max_weight


def fixture(length=5):
    weights = [random.randint(1, 10) for i in range(length)]
    print(weights)
    values = [random.randint(2, 20) for i in range(length)]
    print(values)
    return weights, values


if __name__ == '__main__':
    weights, values = fixture(5)
    bag_weight = 8
    bag = Bag()
    value, weight = bag.solution(weights, values, bag_weight)
    print(f"value: {value}  weight:{weight}")
