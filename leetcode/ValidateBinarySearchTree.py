#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: ValidateBinarySearchTree.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-07-23 19:43
# @Last Modified: 2019-07-23 19:43


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        p = None
        for i in self._in(root):
            if p is None or i > p:
                p = i
            else:
                return False
        return True

    def _in(self, node):
        if node.left is not None:
            yield from self._in(node.left)

        yield node.val

        if node.right is not None:
            yield from self._in(node.right)

if __name__ == '__main__':
    t = TreeNode(0)
    t.right = TreeNode(1)
    s = Solution()
    print(s.isValidBST(t))
