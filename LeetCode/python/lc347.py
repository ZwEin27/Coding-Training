class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ht = {}
        for num in nums:
            ht.setdefault(num, 0)
            ht[num] += 1

        # for (k, v) in ht.items():
        nums = sorted(ht.items(), key=lambda x: x[1], reverse=True)
        nums = [_[0] for _ in nums]
        # print nums
        # nums = nums.keys()
        return nums[:k]

nums = [1,1,1,2,2,3]
k = 2

print Solution().topKFrequent(nums, k)
