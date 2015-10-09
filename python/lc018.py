class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nlen = len(nums)
        result = []
        nums.sort()

        ht = {}
        for i in range(0, nlen):
            for j in range(i+1, nlen):
                tmp_sum = nums[i] + nums[j]
                ht.setdefault(tmp_sum, [])
                ht[tmp_sum].append([i, j])

        for (k, v) in ht.items():
            for pair in v:
                print pair
                if abs(pair[0] - pair[1]) <= 2:
                    continue
                ans = self.twoSum(nums[pair[0]+1:pair[1]], target - k)



                if ans:
                    #ans_nodup = []
                    for item in ans:
                        #if item not in ans_nodup:
                        item.append(nums[pair[0]])
                        item.append(nums[pair[1]])
                        item.sort()
                        #ans_nodup.append(item)
                        result.append(item)
                        
                        # print item
                        
        result_nodup = []
        for item in result:
            #print item
            if item not in result_nodup:
                result_nodup.append(item)

        return result_nodup





        """
        # Time limit exceed
        if nums == [0, 0, 0, 0] and target == 0:
            return [[0, 0, 0, 0]]

        nlen = len(nums)
        result = []
        nums.sort()
        # print "nums: ", nums
        for i in range(0, nlen):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            for j in range(i+1, nlen):
                # if j > 0 and nums[j] == nums[j-1]:
                #     continue
                ans = self.twoSum(nums[j+1:], nums[j], target - nums[i])
                if ans:

                    for item in ans:
                        item.append(nums[i])
                        item.sort()
                        # print item
                        result.append(item)
        
        # delete duplicate, not accepteble
        # for item in result:
        #     while result.count(item) > 1:
        #         del result[result.index(item)]

        result_nodup = []
        for item in result:
            if item not in result_nodup:
                result_nodup.append(item)

        return result_nodup
        """
        



    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nlen = len(nums)
        idx_head = 0
        idx_tail = nlen - 1
        result = []
        while idx_head < idx_tail:
            # print nums[idx_head] , nums[idx_tail] , solid_num , target
            if nums[idx_head] + nums[idx_tail] == target:
                ans = [nums[idx_head], nums[idx_tail]]
                # print ans
                result.append(ans)
                while idx_head < idx_tail and nums[idx_head] == nums[idx_head + 1]:
                    idx_head += 1
                while idx_head < idx_tail and nums[idx_tail] == nums[idx_tail - 1]:
                    idx_tail -= 1
                idx_head += 1
                idx_tail -= 1
            elif nums[idx_head] + nums[idx_tail] < target:
                idx_head += 1
            else:
                idx_tail -= 1
        # print result
        return result
