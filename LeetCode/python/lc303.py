class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.nums_len = len(nums)
        self.dp = [0]*(self.nums_len + 1)
        for i in range(1, self.nums_len+1):
            self.dp[i] = self.dp[i-1] + self.nums[i-1]


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1] - self.dp[i+1] + self.nums[i]



# Your NumArray object will be instantiated and called as such:

nums = [-2, 0, 3, -5, 2, -1]

numArray = NumArray(nums)
print numArray.sumRange(0, 5)
# print numArray.dp
# numArray.sumRange(1, 2)