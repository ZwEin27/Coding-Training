# http://bookshadow.com/weblog/2015/08/17/leetcode-single-number-iii/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        xor = reduce(lambda x,y: x^y, nums)    # same num will be filter by xor
        lowbit = xor & -xor                     # first diff bit for the target two nums
        a, b = 0, 0
        for num in nums:
            if num & lowbit:                    # distinguish the target two nums
                a ^= num                        # same nums will be filter
            else:
                b ^= num
        return [a, b]








nums = [1, 2, 1, 3, 2, 5]
Solution().singleNumber(nums)
