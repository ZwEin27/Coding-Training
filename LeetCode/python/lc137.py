class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            count = 0
            for n in nums:
                count += (n >> i) & 1
            rem = count % 3
            if i == 31 and rem:  # must handle the negative case
                print res
                res -= 1 << 31
            else:
                res |= rem << i
        return res

nums = [1,1,1,-1]
print Solution().singleNumber(nums)
