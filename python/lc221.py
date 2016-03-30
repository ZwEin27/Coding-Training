# http://bookshadow.com/weblog/2015/06/03/leetcode-maximal-square/
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])

        dp = [[0] * n for _ in xrange(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j])
                if i and j and dp[i][j]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                ans = max(ans, dp[i][j])
        return ans

matrix = ['1']
print Solution().maximalSquare(matrix)