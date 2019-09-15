#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: LeafSimilarTrees.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-09-15 09:28
# @Last Modified: 2019-09-15 09:28


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l = self.iter_tree(root1)
        r = self.iter_tree(root2)
        while 1:
            try:
                left = next(l)
            except StopIteration:
                left = None

            try:
                right = next(r)
            except StopIteration:
                right = None
                if left == right:
                    return True
                else:
                    return False

            if left == right:
                pass
            else:
                return False

    def iter_tree(self, root):
        if root.left is None and root.right is None:
            yield root.val
        else:
            if root.left is not None:
                yield from self.iter_tree(root.left)
            if root.right is not None:
                yield from self.iter_tree(root.right)


class Tree:
    root = None

    def __init__(self):
        self.root = TreeNode(10)

    def insert(self, val):
        node = TreeNode(val)
        self._insert(self.root, node)

    def _insert(self, root, node):
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                self._insert(root.right, node)

        else:
            if root.left is None:
                root.left = node
            else:
                self._insert(root.left, node)


if __name__ == '__main__':
    s = Solution()
    t1 = Tree()
    t2 = Tree()
    assert s.leafSimilar(t1.root, t2.root)
    for i in [3, 5, 12, 1, 16, 7, 9, 14]:
        t1.insert(i)

    for i in [3, 5, 12, 1, 16, 7, 9, 14]:
        t2.insert(i)
    assert s.leafSimilar(t1.root, t2.root)
