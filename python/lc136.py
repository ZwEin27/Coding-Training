class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        nums.sort()
        nlen = len(nums)

        if nlen == 1:
            return nums[0]

        for i in range(0, nlen/2):
            d1 = nums[2*i]
            d2 = nums[2*i + 1]

            if d1 != d2:
                return d1

        # print i #9999

        return nums[2*(i+1)]






        
        """
        # 76ms
        nlen = len(nums)
        ht = {}
        for i in range(nlen):
            cur = nums[i]
            # ht.setdefault(cur, 1)
            if ht.has_key(cur):
                ht[cur] += 1
            else:
                ht[cur] = 1

        # print ht

        for (k, v) in ht.items():
            if v == 1:
                return k
        """