#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: MergeSortedLists.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 合并多个有序列表
# https://leetcode.com/problems/merge-k-sorted-lists/
# @Create: 2019-07-20 17:24
# @Last Modified: 2019-07-20 17:24

from typing import List
from queue import PriorityQueue
import sys


class ListNode:
    __slots__ = 'val', 'next'

    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        return self.val < other.val


class MergeSortedLists:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(None)
        tail = head
        q = PriorityQueue()
        for node in lists:
            if node: q.put(node)
        while q.qsize() > 0:
            tail.next = q.get()
            tail = tail.next
            if tail.next: q.put(tail.next)
        return head.next


def print_list(data):
    if data is None:
        return
    p = data
    while p.next is not None:
        print(p.val, end='->')
        p = p.next
    print(p.val)


if __name__ == "__main__":
    data = [
        [5, 4, 1],
        [4, 3, 1],
        [6, 2]
    ]

    input = list()
    for l in data:
        head = ListNode(None)
        for d in l:
            t = ListNode(d)
            t.next = head.next
            head.next = t
        input.append(head.next)
    for l in input:
        print_list(l)
    m = MergeSortedLists()
    # input = [None, None]
    output = m.mergeKLists(input)
    print_list(output)

