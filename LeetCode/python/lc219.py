class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        nlen = len(nums);
        ht = dict();
        for i in range(nlen):
            num = nums[i];
            if ht.has_key(num) and abs(ht[num] - i) <= k:
                return True;
            ht[num] = i;
        return False;
