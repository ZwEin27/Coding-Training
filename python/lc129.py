# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        val_list = self.dfs(root)
        sum = 0
        for val in val_list:
            sum += int(val)
        return sum

    def dfs(self, node):
        # stack = []
        # visited = []
        # if ndoe:
        #     stack.append(root)

        # while stack:
        # cur = stack.pop(-1)
        # visited.append(cur.val)

        val_list = []

        if node.left:
            vals = self.dfs(node.left)
            for val in vals:
                val_list.append(node.val+val)

        if node.right:
            vals = self.dfs(node.right)
            for val in vals:
                val_list.append(node.val+val)

        if len(val_list) == 0:
            return [node.val]

        return val_list

