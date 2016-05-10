class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        if not nums:
            return []
        ans = []
        visited = [0]*len(nums)
        self.search(ans, [], visited, sorted(nums))
        return ans

    def search(self, ans, alist, visited, nums):
        if len(alist) == len(nums):
            ans.append(list(alist))

        for i in range(len(nums)):
            if visited[i] or (i != 0 and nums[i] == nums[i-1] and visited[i-1] == 0):
                continue
            visited[i] = 1
            self.search(ans, alist + [nums[i]], visited, nums)
            visited[i] = 0
