
# https://leetcode.com/discuss/82822/solution-explanation
# http://bookshadow.com/weblog/2016/01/27/leetcode-patching-array/
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        idx, total, ans = 0, 1, 0
        size = len(nums)
        while total <= n:
            if idx < size and nums[idx] <= total:
                total += nums[idx]
                idx += 1
                print 'up'
                print total
            else:
                print 'down'
                total <<= 1
                ans += 1
        return ans


nums = [1, 3]
n = 6
print Solution().minPatches(nums, n)