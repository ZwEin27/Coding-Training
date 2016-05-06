class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # http://www.tuicool.com/articles/RZZnQf

        x = 5
        ans = 0
        while n >= x:
          ans += n / x
          x *= 5
        return ans