# http://bookshadow.com/weblog/2015/01/13/leetcode-largest-number/
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        num = sorted([str(num) for num in nums], cmp=self.compareInt)
        ans = ''.join(num).lstrip('0')
        return ans or '0'

    def compareInt(self, a, b):
        return [1,-1][a+b>b+a]


# nums = [3, 30, 34, 5, 9]
nums = [0,0,0,0]
print Solution().largestNumber(nums)