class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #http://courses.csail.mit.edu/6.006/spring11/lectures/lec02.pdf
        nlen = len(nums)
        left = 0
        right = nlen - 1
        while left <= right:
            if left == right:
                return left
            mid = (left + right)/2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
