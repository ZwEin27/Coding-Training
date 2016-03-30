class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x

        while left <= right:
            mid = (left + right) / 2
            if mid ** 2 <= x and x < (mid + 1) **2:
                return mid
            if mid ** 2 > x:
                right -= 1
            else:
                left += 1
x = 6
print Solution().mySqrt(x)