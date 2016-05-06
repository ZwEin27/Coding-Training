class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # http://bookshadow.com/weblog/2015/02/24/leetcode-rotate-array/
        numslen = len(nums);
        if k > 0 and numslen > 1:
            idx = numslen - k;
            nums[:] = nums[idx:numslen] + nums[0:idx];
        
        