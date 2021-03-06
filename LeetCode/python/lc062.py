class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # http://www.tuicool.com/articles/R3yyAf

        if m ==0 or n == 0:
            return 0

        dp = [[0 for col in range(n)] for row in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            dp[i][0] = 1
        for j in range(1, n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
