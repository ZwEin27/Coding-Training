# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return None

        return self.func(nums, 0, len(nums)-1)


    def func(self, nums, start, end):
        if start == end:
            return TreeNode(nums[start])


        mid = (start + end) / 2
        node = TreeNode(nums[mid])
        if start < mid:
            node.left = self.func(nums, start, mid-1)
        if mid < end:
            node.right = self.func(nums, mid+1, end)
        return node


        node.left
