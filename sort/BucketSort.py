#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: BucketSort.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-06-13 20:12
# @Last Modified: 2019-06-13 20:12

from typing import List
import array
import random
from itertools import chain


class BucketSort:

    def bucket_sort(self, data: array, n=100) -> List:
        buckets = [array.array('l') for _ in range(n)]
        for d in data:
            buckets[d].append(d)
        return array.array('l', chain(*buckets))


def test():
    a = [random.randint(0,99) for _ in range(200)]
    data = array.array('l', a)
    print(data)
    bs = BucketSort()
    data = bs.bucket_sort(data)
    print(data)


if __name__ == "__main__":
    test()