class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for num in nums:
            s.add(num)

        max_value = 0
        for num in nums:
            if num-1 not in s:
                val = num
                while val in s:
                    s.discard(val)
                    val += 1
                max_value = max(max_value, val - num)
        return max_value



nums = [100, 4, 200, 1, 3, 2]
print Solution().longestConsecutive(nums)
