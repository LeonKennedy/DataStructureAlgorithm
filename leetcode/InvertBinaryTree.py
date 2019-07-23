#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: InvertBinaryTree.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-07-23 19:04
# @Last Modified: 2019-07-23 19:04


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

    def invertTree2(self, root: TreeNode) -> TreeNode:




