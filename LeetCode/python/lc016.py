class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        nlen = len(nums)
        nums.sort()
        result = [-1000, 0, 0, 0]
        for i in range(nlen):
            if i > 0 and nums[i] == nums[i-1]:
                continue; 
            ans = self.twoSum(nums[i+1:], nums[i], target)
            if ans[0] == target:
                return ans[0]
            if abs(ans[0] - target) < abs(result[0] - target):
                    result = ans
        return result[0]

        # return self.twoSum(nums, nums[0])


    def twoSum(self, nums, solid_num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nlen = len(nums)
        idx_head = 0
        idx_tail = nlen - 1
        result = [-1000, 0, 0, 0]


        while idx_head < idx_tail:

            thr_sum = nums[idx_head] + nums[idx_tail] + solid_num
            #print thr_sum
            # ans = [solid_num, nums[idx_head], nums[idx_tail]]
            if thr_sum == target:
                
                #print ans
                return [thr_sum, solid_num, nums[idx_head], nums[idx_tail]]
                # while idx_head < idx_tail and nums[idx_head] == nums[idx_head + 1]:
                #     idx_head += 1
                # while idx_head < idx_tail and nums[idx_tail] == nums[idx_tail - 1]:
                #     idx_tail -= 1
                # idx_head += 1
                # idx_tail -= 1
            elif thr_sum < target:
                if abs(thr_sum - target) < abs(result[0] - target):
                    result = [thr_sum, solid_num, nums[idx_head], nums[idx_tail]]
                idx_head += 1
            else:
                if abs(thr_sum - target) < abs(result[0] - target):
                    result = [thr_sum, solid_num, nums[idx_head], nums[idx_tail]]
                idx_tail -= 1

        return result
