# https://leetcode.com/discuss/95367/1ms-java-solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_rob, max_no_rob = self.do_rob(root)
        return max(max_rob, max_no_rob)

    def do_rob(self, node):
        if not node:
            return 0, 0
        else:
            left_max_rob, left_max_no_rob = self.do_rob(node.left)
            right_max_rob, right_max_no_rob = self.do_rob(node.right)

            max_rob = left_max_no_rob + right_max_no_rob + node.val
            max_no_rob = max(left_max_rob, left_max_no_rob) + max(right_max_rob, right_max_no_rob)

        return max_rob, max_no_rob
