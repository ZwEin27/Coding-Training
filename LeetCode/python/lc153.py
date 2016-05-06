class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # http://blog.csdn.net/ljiabin/article/details/40296977
        nlen = len(nums)
        if nlen == 1:
            return nums[0]

        left = 0
        right = nlen - 1
        while nums[left] > nums[right]:
            mid = (left + right) / 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
