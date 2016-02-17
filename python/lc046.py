class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums_len = len(nums)
        if nums_len == 0:
            return [[]]
        if nums_len == 1:
            return [nums]


        for i in range(nums_len):
            num = nums[i]
            tmp = list(nums)
            del tmp[i]
            rtn_list = self.permute(tmp)
            for j in range(len(rtn_list)):
                tmp = [num]
                tmp.extend(rtn_list[j])
                result.append(tmp)
        return result


nums = [1,2,3]
print Solution().permute(nums)