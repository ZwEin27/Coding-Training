class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        size = len(nums)
        if size < 2:
            return 0
        nums.sort()
        max_value = 0
        for i in range(1, size):
            gap = nums[i] - nums[i-1]
            if gap > max_value:
                max_value = gap
        return max_value
