class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        nlen = len(nums)
        
        nums_ht = {}    # hash table, key for nums's index, value for nums's value

        # load data for hash table
        for i in range(nlen):
            nums_ht[i] = nums[i]

        # hash table, key-value pairs
        nums_ht_items = nums_ht.items()

        # use value as key, this step is for store duplicate items
        backitems = [[v[1], v[0]] for v in nums_ht_items]
        # sort by value
        backitems.sort()
        # return sorted idx, for min to max
        idxs_sorted = [ backitems[i][1] for i in range(0,len(backitems))]

        idx_head = 0    # idx for sorted
        idx_tail = nlen - 1     # idx for sorted
        while idx_head < idx_tail:

            twosum = nums[idxs_sorted[idx_head]] + nums[idxs_sorted[idx_tail]]

            if twosum == target:
                result = [idxs_sorted[idx_head] + 1, idxs_sorted[idx_tail] + 1]
                result.sort()
                return result
            if twosum < target:
                idx_head += 1
            if twosum > target:
                idx_tail -= 1

        return []
