# https://segmentfault.com/a/1190000003768736
# https://leetcode.com/discuss/70626/accepted-recursive-solution-in-python-using-memoization
import sys
class Solution(object):

    def __init__(self):
        self.dp = [sys.maxint] * (10001)
        # i = 0
        # while i*i <= n:
        #     dp[i*i] = 1
        #     i += 1
        # cache = [0] * 10001

        for i in range(1, 101):
            self.dp[i**2] = 1

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        for a in range(1, n+1):
            b = 1
            while a+b*b <= n:
                self.dp[a+b*b] = min(self.dp[a+b*b], self.dp[a]+1)
                b += 1
        return self.dp[n]



"""
# time excceed

        if n <= 0:
            return 0

        val_list = self.bfs(n)
        if len(val_list) == 0:
            return 0 

        min_len = val_list[1]
        for val in val_list:
            if len(val) < min_len:
                min_len = len(val)
        return min_len

    def bfs(self, n):
        if n == 0:
            return []
        if n < 0:
            return None

        val_list = []

        i = 1
        while i*i <= n:
            tmp = self.bfs(n-i*i)
            if tmp:
                tmp.extend(i*i)
                val_list.append(tmp)
            i += 1
        return val_list
"""