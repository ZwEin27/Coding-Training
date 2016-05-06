class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        nlen = len(nums)
        idx = 0
        count = 0

        while idx < nlen - count :
            cur = nums[idx]
            if cur == 0:
                del nums[idx]
                nums.append(0)
                count += 1
            else:
                idx += 1
        
        # print nums