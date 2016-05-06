#!/usr/bin/env python
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        pre = -100;
        idx = 0;
        while idx < len(nums):
            cur = nums[idx];
            if (cur == pre):
                del nums[idx];
            else:
                pre = cur;
                idx = idx + 1;
        return len(nums);

