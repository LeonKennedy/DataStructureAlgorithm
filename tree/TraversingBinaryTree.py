#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: TraversingBinaryTree.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-06-18 20:04
# @Last Modified: 2019-06-18 20:04


class TraversingBinaryTree:

    def __init__(self):
        self._list = [None]

    def __str__(self):
        return str(self._list)

    def append(self, value):
        self._list.append(value)

    def pre_traversing(self):
        i = 1
        yield from self._ccc(i)

    def _pre(self, i):
        yield self._list[i]
        left = i * 2
        try:
            if self._list[left] is not None:
                yield from self._pre(left)
        except IndexError:
            pass
        right = i * 2 + 1
        try:
            if self._list[right] is not None:
                yield from self._pre(right)
        except IndexError:
            pass

    def in_traversing(self):
        yield from self._bbb(1)

    def _in(self, i):
        left = i * 2
        try:
            if self._list[left] is not None:
                yield from self._in(left)
        except IndexError:
            pass
        yield self._list[i]
        right = i * 2 + 1
        try:
            if self._list[right] is not None:
                yield from self._in(right)
        except IndexError:
            pass

    def post_traversing(self):
        yield from self._ddd(1)

    def _post(self, i):
        left = i * 2
        try:
            if self._list[left] is not None:
                yield from self._post(left)
        except IndexError:
            pass

        right = i * 2 + 1
        try:
            if self._list[right] is not None:
                yield from self._post(right)
        except IndexError:
            pass
        yield self._list[i]


if __name__ == "__main__":
    tree = TraversingBinaryTree()
    for i in 'ABCDEFG':
        tree.append(i)
    print(tree)
    print('pre')
    for i in tree.pre_traversing():
        print(i, end=' ')
    print('\nmid')
    for i in tree.in_traversing():
        print(i, end=' ')
    print('\nlast')
    for i in tree.post_traversing():
        print(i, end=' ')