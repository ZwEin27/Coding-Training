class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = [0]*(target+1)
        for cur_target in range(1, len(ans)):
            for num in nums:
                if num > cur_target:
                    break
                elif num == cur_target:
                    ans[cur_target] += 1
                else:
                    ans[cur_target] += ans[cur_target-num]
        return ans[target]




"""
class Solution(object):
    def combinationSum4(self, nums, target):
        self.ans = 0
        self.search([], sorted(nums), target)
        return self.ans

    def search(self, alist, nums, target):

        if target == 0:
            self.ans += 1
            return

        for num in nums:
            if num <= target:
                self.search(alist+[num], nums, target-num)
            else:
                return

"""

        
