class Solution(object):

    def minSubArrayLen(self, s, nums):
        size = len(nums)
        left, right = 0, size

        best = 0
        while left <= right:
            window_size = (left + right) / 2
            if self.containSum(window_size, s, nums):
                best = window_size
                right = window_size - 1
            else:
                left = window_size + 1
        return window_size

    def containSum(self, window_size, s, nums):
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if i >= window_size:
                sums -= nums[i - window_size]
            if sums >= s:
                return True
        return False




"""
    def minSubArrayLen(self, s, nums):
        # O(n)
        size = len(nums)
        left, right, summary = 0, 0, 0
        best = size + 1
        while right < size:
            while right < size and summary < s:
                summary += nums[right]
                right += 1
            while left < right and summary >= s:
                best = min(best, right - left)
                summary -= nums[left]
                left += 1
        if best <= size:
            return best
        else:
            return 0
"""



s = 7
nums = [2,3,1,2,4,3]
print Solution().minSubArrayLen(s, nums)
