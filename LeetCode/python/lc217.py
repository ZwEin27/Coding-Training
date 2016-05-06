class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ht = {};

        for i in range(0, len(nums)):
            num = nums[i];
            if ht.has_key(num):
                return True;
            else:
                ht[num] = 1;
        return False;