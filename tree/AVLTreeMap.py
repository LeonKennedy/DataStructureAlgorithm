#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: AVLTreeMap.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-08-20 14:57
# @Last Modified: 2019-08-20 14:57

from typing import TypeVar

from TreeMap import TreeMap

NodeElement = TypeVar('NodeElement')


class AVLTreeMap(TreeMap):
    class _Node:
        __slots__ = "val", "_h", "left", "right", "p"

        def __init__(self, element: NodeElement):
            self.val = element
            self._h = 1
            self.left = None
            self.right = None
            self.p = None

        @property
        def height(self) -> int:
            if self._h is None:
                left_height = 0 if self.left is None else self.left.height
                right_height = 0 if self.right is None else self.right.height
                self._h = max(left_height, right_height) + 1
            return self._h

        def refresh_height(self) -> None:
            self._h = None

    def insert(self, value: int) -> None:
        node = self._Node(value)
        if self._head is None:
            self._head = node
            return True
        else:
            self._insert(self._head, node)

    def _insert(self, root: _Node, node: _Node):
        if root.val > node.val:
            if root.left is None:
                root.left = node
                node.p = root
                child = node
            else:
                child = self._insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
                node.p = root
                child = node
            else:
                child = self._insert(root.right, node)

        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if left_height - right_height > 1:
            child = root.left
            if self.height(child.left) > self.height(child.right):
                self.rotate(child)
            else:
                cc = root.left.right
                self.rotate(cc)
                self.rotate(cc)

            left_height = self.height(child.left)
            right_height = self.height(child.right)
            child._h = max(left_height, right_height) + 1
            return child
        elif right_height - left_height > 1:
            child = root.right
            if self.height(child.left) < self.height(child.right):
                self.rotate(child)
            else:
                cc = root.right.left
                self.rotate(cc)
                self.rotate(cc)

            left_height = self.height(child.left)
            right_height = self.height(child.right)
            child._h = max(left_height, right_height) + 1
            return child
        else:
            root._h = max(root.height, child.height + 1)
            return root

    def height(self, node):
        return 0 if node is None else node.height

    def rotate(self, node):
        father = node.p
        grandfather = father.p
        if father.left == node:
            self.relink(father, node, True)
        else:
            self.relink(father, node, False)

        if grandfather is None:
            self._head = node
            node.p = None
        else:
            node.p = grandfather
            if grandfather.val > node.val:
                grandfather.left = node
            else:
                grandfather.right = node

    def relink(self, a, b, left):
        # 1
        if left:
            a.left = b.right
            b.right = a
        else:
            a.right = b.left
            b.left = a

        a.refresh_height()
        a.p = b

    def delete(self, value):
        pass
    
    def _rebalance_insert(self, p):
        super()._rebalance_insert(p)

    def _rebalance_delete(self, p):
        super()._rebalance_delete(p)

    def _rebalance_access(self, p):
        super()._rebalance_access(p)


if __name__ == '__main__':
    avl = AVLTreeMap()
    for i in (100, 5, 7, 3, 1, 8, 9, 13, 15, 19, 22):
        avl.insert(i)
    for i in avl:
        print(i)
