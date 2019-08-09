#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: PathSum.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-08-09 14:40
# @Last Modified: 2019-08-09 14:40

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if sum == root.val and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)