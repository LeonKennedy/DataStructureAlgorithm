#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: mheapq.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description:
# @Create: 2019-07-23 10:21
# @Last Modified: 2019-07-23 10:21
import heapq
from heapq import _heapify_max, _siftdown_max, _siftup_max, _heapreplace_max
from typing import List


class CoffeeHeapq:
    """
        implement  heap max
    """

    def __init__(self):
        self._d = list()

    @property
    def len(self):
        return len(self._d)

    @property
    def top(self):
        if len(self._d) == 0:
            raise ValueError
        return self._d[0]

    def pop(self) -> int:
        if len(self._d) == 1:
            return self._d.pop()
        top = self.top
        self._d[0] = self._d.pop()
        p = 0
        while p * 2 + 2 < self.len:
            mi = max(p, p * 2 + 1, p*2+2, key=lambda x: self._d[x])
            if mi > p:
                self._d[mi], self._d[p] = self._d[p], self._d[mi]
                p = mi
            else:
                break
        if p *2+1 < self.len and self._d[p *2+1] > self._d[p]:
            self._d[p], self._d[2*p+1] = self._d[2*p+1], self._d[p]
        return top

    def push(self, item):
        self._d.append(item)
        p = self.len - 1
        q = self.get_parent(p)
        while q >= 0:
            if self._d[p] > self._d[q]:
                self._d[p], self._d[q] = self._d[q], self._d[p]
                p, q = q, self.get_parent(q)
            else:
                break

    def get_parent(self, p: int) -> int:
        if p % 2 == 0:
            return (p - 2) // 2
        else:
            return (p - 1) // 2

    def _insert(self, item, p):
        if p == self.len:
            self._d.append(item)


class MaxHeapq:
    def __init__(self, maxsize):
        self._heap = list()

    def __len__(self):
        return len(self._heap)

    def top(self):
        if len(self._heap) == 0:
            raise ValueError
        return self._heap[0]

    def extends(self, items: List):
        _heapify_max(items)
        self._items = items

    def pop(self):
        lastelt = self._heap.pop()    # raises appropriate IndexError if heap is empty
        if self._heap:
            returnitem = self._heap[0]
            self._heap[0] = lastelt
            _siftup_max(self._heap, 0)
            return returnitem
        return lastelt

    def push(self, item):
        self._heap.append(item)
        _siftdown_max(self._heap, 0, len(self._heap) - 1)

    def replace(self, item, out_item):
        i = self._heap.index(item)
        self.uper_son(i)

    def uper_son(self, index):
        pass

    # def __str__(self):
    #     heapqsor
# def heappush(heap, item):
#     """Push item onto heap, maintaining the heap invariant."""
#     heap.append(item)
#     _siftdown_max(heap, 0, len(heap)-1)
#
# def heappop(heap):
#     """Pop the smallest item off the heap, maintaining the heap invariant."""
#     lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
#     if heap:
#         returnitem = heap[0]
#         heap[0] = lastelt
#         _siftup_max(heap, 0)
#         return returnitem
#     return lastelt


if __name__ == '__main__':
    mpq = MaxHeapq(5)
    data = [1,7,34,2,5,7,9,3,2]
    for d in data:
        mpq.push(d)
    while len(mpq):
        print(mpq.pop(), end=' ')
    print()
    print('_' * 50)
    cpq = CoffeeHeapq()
    data = [1, 7, 34, 2, 5, 7, 9, 3, 2]
    for d in data:
        cpq.push(d)
    while cpq.len:
        print(cpq.pop(), end=' ')
