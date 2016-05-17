class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        matrix = [0]* (size+1)

        for num in nums:
            matrix[num] += 1

        return matrix.index(max(matrix))

nums = [1,2,3,5,5,5]
print Solution().findDuplicate(nums)
