# http://www.tuicool.com/articles/ZjEzqme

class Solution(object):
    
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        import random
        pivot = random.choice(nums)
        num1, num2 = [], []

        for num in nums:
            if num > pivot:
                num1.append(num)
            elif num < pivot:
                num2.append(num)

        size_num1 = len(num1)
        size_num2 = len(num2)
        size_nums = len(nums)

        if k <= size_num1:
            return self.findKthLargest(num1, k)
        if k > size_nums - size_num2:
            return self.findKthLargest(num2, k - (size_nums - size_num2))
        return pivot

        