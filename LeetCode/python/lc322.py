#   http://bookshadow.com/weblog/2015/12/27/leetcode-coin-change/

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [0] + [-1] * amount


        for x in range(amount+1):
            if dp[x] < 0:
                continue
            for c in coins:
                if x+c <= amount:
                    if dp[x+c] < 0 or dp[x+c] > dp[x]+1:
                        dp[x+c] = dp[x] + 1
                    
        return dp[-1] 


coins = [1,2,5]
amount = 11
print Solution().coinChange(coins, amount)
