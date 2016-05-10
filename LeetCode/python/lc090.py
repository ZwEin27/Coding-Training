class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        if not S or len(S) == 0:
            return None
        ans = []
        self.search(ans, [], sorted(S), 0)
        return ans

    def search(self, ans, alist, nums, pos):
        ans.append(list(alist))

        for i in range(pos, len(nums)):
            if i != pos and nums[i] == nums[i-1]:
                continue
            self.search(ans, alist + [nums[i]], nums, i+1)
            
