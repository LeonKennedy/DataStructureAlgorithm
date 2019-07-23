#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: SlidingWindowMaximum.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: https://leetcode.com/problems/sliding-window-maximum/ 滑动窗口最大值
# @Create: 2019-07-22 19:06
# @Last Modified: 2019-07-22 19:06

from typing import List
from queue import PriorityQueue
import random
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0 :
            return []
        dq = deque()
        res = []
        for i in range(len(nums)):
            if dq and dq[0] < i - k +1:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i > k - 2:
                res.append(nums[dq[0]])
        return res

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        """
         bad method  随着k的增加 效果比方法一差
        :param nums:
        :param k:
        :return:
        """
        if not nums or k == 0:
            return []
        queue = list()
        res = []
        for i, num in enumerate(nums):
            for key, v in enumerate(queue):
                if num > v:
                    queue.insert(key, num)
                    break
            else:
                queue.append(num)
            if i > k - 2:
                res.append(queue[0])
                queue.remove(nums[i-k+1])
        return res

data, k = [random.randint(-100, 1000) for _ in range(1000)], 20

def test1():
    s = Solution()
    output = s.maxSlidingWindow(data, k)

def test2():
    s = Solution()
    output = s.maxSlidingWindow2(data, k)

if __name__ == '__main__':
    s = Solution()
    output = s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
    print(output)
    test1()