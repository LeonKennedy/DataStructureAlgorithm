#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: MajorityElement.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 求众数。 假设：数组不为空，必定存在众数
#  解法  摩尔投票
# @Create: 2019-07-18 17:18
# @Last Modified: 2019-07-18 17:18

from typing import List


class MajorityElement:

    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        for v in nums[1:]:
            if counter == 0:
                major = v
                counter += 1
            elif major == v:
                counter += 1
            else:
                counter -= 1
        return major


if __name__ == "__main__":
    me = MajorityElement()
    nums = [1,1,1,1,2,2]
    output = me.majorityElement(nums)
    print(output)