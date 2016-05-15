class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        min_value = num[0]
        for i in num:
            if i < min_value:
                min_value = i
        return min_value
