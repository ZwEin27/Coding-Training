# http://bookshadow.com/weblog/2015/11/30/leetcode-burst-balloons/

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_list = [1] + nums + [1]
        size = len(num_list)
        dp = [[0] * size for _ in range(size)]

        for k in range(2, size):
            for l in range(0, size-k):
                r = l + k
                for m in range(l+1, r):
                    dp[l][r] = max(dp[l][r], num_list[l] * num_list[m] * num_list[r] + dp[l][m] + dp[m][r])

        return dp[0][-1]






nums = [3, 1, 5, 8]
print Solution().maxCoins(nums)

