#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: ThreeSum.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-07-18 16:11
# @Last Modified: 2019-07-18 16:11
from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [0, 0, 0, 0]
    output = s.threeSum(nums)
    print(output)
