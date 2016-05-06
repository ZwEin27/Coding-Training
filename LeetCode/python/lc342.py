class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        mask = int('1010101010101010101010101010101', 2)
        return num != 0 and num & mask == num and num & (num-1) == 0



num = 64
print Solution().isPowerOfFour(num)
