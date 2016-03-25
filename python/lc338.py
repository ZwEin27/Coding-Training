class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        dp = [] # 0 * (num + 1)
        dp.append(0)
        dp.append(1)
        
        level = 1

        while len(dp) - 1 < pow(2, level) and num >= len(dp):
            size = len(dp)
            for i in range(size):
                if num < len(dp):
                    break;
                dp.append(dp[i]+1)
            level += 1

        return dp[:num+1]

print Solution().countBits(5)




