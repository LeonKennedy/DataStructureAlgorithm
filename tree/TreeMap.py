#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: TreeMap.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-08-20 14:53
# @Last Modified: 2019-08-20 14:53

from typing import TypeVar

NodeElement = TypeVar('NodeElement')


class TreeMap:
    class _Node:
        __slots__ = "val", "left", "right"

        def __init__(self, element: NodeElement):
            self.val = element

    def __init__(self):
        self._head = None

    def __iter__(self):
        yield from self._in(self._head)

    def _in(self, node: _Node):
        if node.left is not None:
            yield from self._in(node.left)

        yield node.val
        if node.right is not None:
            yield from self._in(node.right)

    def _rebalance_insert(self, p):
        pass

    def _rebalance_delete(self, p):
        pass

    def _rebalance_access(self, p):
        pass
