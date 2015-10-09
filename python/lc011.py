class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        hlen = len(height)
        if hlen == 0:
            return 0

        i = 0
        j = hlen - 1
        maxs = 0

        while 0 <= i and i < j and j < hlen:

            tmp = min(height[i], height[j]) * (j - i)
            maxs = max(tmp, maxs)

            if height[i] < height[j]:
                k = i
                while k < j and height[k] <= height[i]:
                    k += 1
                i = k
            else:
                k = j
                while i < k and height[k] <= height[j]:
                    k -= 1
                j = k

        return maxs


        


