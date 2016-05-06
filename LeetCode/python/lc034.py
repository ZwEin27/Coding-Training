class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        nlen = len(nums)
        if nlen == 0:
            return [-1, -1]

        idx = self.search(nums, 0, nlen-1, target)
        if idx == -1:
            return [-1, -1]

        # print idx

        i = idx - 1
        while i >= 0:
            if nums[i] != target:
                break
            i -= 1
        if i >= 0:
            idx_start = i + 1
        else:
            idx_start = 0

        i = idx + 1
        while i < nlen:
            if nums[i] != target:
                break
            i += 1
        if i < nlen:
            idx_end = i - 1
        else:
            idx_end = nlen - 1

        return [idx_start, idx_end]




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



