class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nlen = len(nums)
        nums.sort()
        result = []
        for i in range(nlen):
            if i > 0 and nums[i] == nums[i-1]:
                continue; 
            result += self.twoSum(nums[i+1:], nums[i])
        return result

        # return self.twoSum(nums, nums[0])


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
            #print nums[idx_head] , nums[idx_tail] , target
            if nums[idx_head] + nums[idx_tail] + target == 0:
                ans = [target, nums[idx_head], nums[idx_tail]]
                #print ans
                result.append(ans)
                while idx_head < idx_tail and nums[idx_head] == nums[idx_head + 1]:
                    idx_head += 1
                while idx_head < idx_tail and nums[idx_tail] == nums[idx_tail - 1]:
                    idx_tail -= 1
                idx_head += 1
                idx_tail -= 1
            elif nums[idx_head] + nums[idx_tail] + target < 0:
                idx_head += 1
            else:
                idx_tail -= 1
        return result
