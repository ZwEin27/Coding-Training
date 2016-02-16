# https://www.hrwhisper.me/leetcode-increasing-triplet-subsequence/

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_length = len(nums)
        if num_length < 3:
            return False

        n1 = n2 = 1 << 128
        for num in nums:
            if num <= n1:
                n1 = num
            elif num <= n2:
                n2 = num
            else:
                return True
        return False


test = [5,2,5,5,1,5,4]

print Solution().increasingTriplet(test)
