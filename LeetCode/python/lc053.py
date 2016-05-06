import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nsum = 0
        ret = - sys.maxint - 1
        for num in nums:
            nsum = max(nsum + num, num)
            ret = max(nsum, ret)
        return ret
