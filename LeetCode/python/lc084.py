class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        if not height:
            return 0

        size = len(height)
        stack = []
        max_val = 0
        for i in range(size + 1):
            if i == size:
                cur = -1
            else:
                cur = height[i]

            while stack and cur <= height[stack[-1]]:
                h = height[stack.pop()]
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1
                max_val = max(max_val, h * w)
            stack.append(i)
        return max_val
