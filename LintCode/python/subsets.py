class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        if not S and len(S) == 0:
            return None
        S.sort()
        ans = []
        self.dfs(ans, [], S, 0)
        return ans

    def dfs(self, ans, tlist, nums, pos):
        ans.append(list(tlist))

        for i in range(pos, len(nums)):
            tlist.append(nums[i])
            self.dfs(ans, tlist, nums, i+1)
            tlist.pop(-1)
            
