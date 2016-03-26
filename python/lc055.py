class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
            
        size = len(nums)
        max_jumps = 0
        for i in xrange(size - 1):
            if  i <= max_jumps:
                max_jumps = max(max_jumps, i + nums[i])

        if max_jumps >= size - 1:
            return True
        else:
            return False
    
                


nums = [2, 0]

print Solution().canJump(nums)




""" TLE
size = len(nums)
        dp = [False] * size
        dp[0] = True
        max_jumps = 0
        for i in range(size - 1):
            if dp[i] or i < max_jumps:
                if i + nums[i] > max_jumps:
                    max_jumps = i + nums[i]
                    if max_jumps >= size:
                        max_jumps = size - 1
                    print max_jumps
                dp[max_jumps] = True
        return dp[-1]
"""