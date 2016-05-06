class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        slen = len(s)
        if slen == 0:
            return 0

        dp = [0] * (slen+1)
        dp[0] = 1
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1
        for i in range(2, slen+1):

            two_digit = int(s[i-2:i])
            if two_digit <= 26 and two_digit >= 10:
                dp[i] += dp[i-2]

            if int(s[i-1]) != 0:
                dp[i] += dp[i-1]

        return dp[-1]


print Solution().numDecodings('122321')