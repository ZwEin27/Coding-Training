class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 152 ms
        # bitmap = 0
        # for num in nums:
        #     bitmap |= 1 << num
        # idx = 0
        # while 1:
        #     if bitmap&(1<<idx) == 0:
        #         return idx
        #     idx += 1

        # 72ms
        sumv = 0
        nlen = len(nums)
        for num in nums:
            sumv += num
        return nlen * (nlen + 1) /2 - sumv





