# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left

        idx = 1
        while stack and idx <= k:
            node = stack.pop(-1)
            tmp = node.right
            idx += 1
            while tmp:
                stack.append(tmp)
                tmp = tmp.left

        return node.val
