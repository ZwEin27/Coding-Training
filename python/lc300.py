class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        size = len(nums)
        dp = [1] * size

        for i in range(size):
            for j in range(i):
                if nums[i] >= nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print dp
        return dp[-1]

nums = [1,3,6,7,9,4,10,5,6]
print Solution().lengthOfLIS(nums)
