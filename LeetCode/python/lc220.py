class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False

        size = len(nums)
        ht = collections.OrderedDict()
        for i in range(size):
            key = nums[i] / max(1, t)
            for m in [key, key+1, key-1]:
                if m in ht and abs(nums[i] - ht[m]) <= t:
                    return True
            ht[key] = nums[i]

            if i >= k:
                ht.popitem(last=False)
        return False
