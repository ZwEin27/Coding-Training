# https://leetcode.com/discuss/94169/time-and-space-python-code-with-comments-beats-69%25-run-times 

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        hlen = len(height)
        if not height or hlen < 3:
            return 0
        total = potential = 0
        tallest = height[0]
        for h in height:
            if tallest <= h:
                total += potential
                potential = 0
                tallest = h
            else:
                potential += tallest - h
        potential = 0
        tallest = height[-1]
        for h in height[::-1]:
            if tallest < h:         # [2, 0, 2]
                total += potential
                potential = 0
                tallest = h
            else:
                potential += tallest - h
        return total



height = [4,2,3]
print Solution().trap(height)
