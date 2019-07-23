#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: MaximumDepthofBinaryTree.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-07-23 19:32
# @Last Modified: 2019-07-23 19:32


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1