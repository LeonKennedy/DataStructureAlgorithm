#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: BaseTree.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-06-18 20:05
# @Last Modified: 2019-06-18 20:05
import random


class Node:

    p = None
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class BinaryTree:

    def __init__(self):
        self._head = None

    def __str__(self):
        return ' '.join(self.in_traversing())

    def append(self, value):
        node = Node(value)
        if self._head is None:
            self._head = node
            return True
        self._append(self._head, node)

    def _append(self, node, new_node):
        x = node
        while x is not None:
            y = x
            if x.value > new_node.value:
                x = x.left
            else:
                x = x.right

        new_node.p = y
        if y.value > new_node.value:
            y.left = new_node
        else:
            y.right = new_node

    def pop(self, value):
        node = self._search(self._head, value)
        self._pop(node)

    def _pop(self, node):
        if node.left is None:
            self._transplant(node, node.right)
            return
        if node.right is None:
            self._transplant(node, node.left)
            return
        successor = self.successor(node.value)
        if successor.p != node:
            self._transplant(successor, successor.right)
            successor.right = node.right
            successor.right.p = successor
        self._transplant(node, successor)
        successor.left = node.left
        successor.left.p = successor

    def _transplant(self, old_node, new_node):
        parents = old_node.p
        if parents.left == old_node:
            parents.left = new_node
        elif parents.right == old_node:
            parents.right = new_node
        if new_node is not None:
            new_node.p = parents

    def _search(self, node, value) -> Node:
        x = node
        while x is not None:
            if x.value > value:
                x = x.left
            elif x.value == value:
                return x
            else:
                x = x.right
        raise ValueError(f"value({value}) is not exist!")

    def _find_son(self, node):
        if node.left is Node:
            return node.right
        if node.right is Node:
            return node.left
        min_node = self._find_most(node.right)
        min_node.left = node.left
        return node.right

    @property
    def min(self):
        return self._find_most(self._head).value

    @property
    def max(self):
        return self._find_most(self._head, minimum=False).value

    def _find_most(self, node, minimum=True) -> Node:
        x = node
        while x is not None:
            y = x
            x = x.left if minimum else x.right
        return y

    def successor(self, value: int) -> Node:
        node = self._search(self._head, value)
        if node.right is not None:
            return node.right
        x = node
        while x.p is not None and x.p.left != x:
            x = x.p
        return None if x.p is None else x.p

    def predecessor(self, value):
        pass

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
        yield from self._in(self._head)

    def _in(self, node):
        if node.left is not None:
            yield from self._in(node.left)

        yield node.value

        if node.right is not None:
            yield from self._in(node.right)

    def post_traversing(self):
        yield from self._post(1)

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
    tree = BinaryTree()
    items = 'MHIPODJGTRASBECX'
    for i in items:
        tree.append(i)
    print(tree)
    print(f"max: {tree.min}")
    print(f"min: {tree.max}")
    print('------')
    item = random.choice(items)
    succ = tree.successor(item)
    print(f" {item} successor is: {succ.value if succ else None}")
    tree.pop(item)
    print(f"after pop {item} : {tree}")
    # tree.pop('F')

