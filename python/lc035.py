class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nlen = len(nums)
        if nlen == 0:
            return [-1, -1]

        idx = self.search(nums, 0, nlen-1, target)
        # print idx
        if idx == -1:
            for i in range(nlen):
                if nums[i] > target:
                    return i
            return nlen
        else:
            return idx




    def search(self, nums, start, end, target):
        mid = (start + end) / 2

        if start > end:
            return -1

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.search(nums, start, mid-1, target)
        else:
            return self.search(nums, mid+1, end, target)