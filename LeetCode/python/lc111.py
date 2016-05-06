# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0;

        # self.depth += 1;

        left_depth = self.minDepth(root.left);
        right_depth = self.minDepth(root.right);

        if left_depth == 0 and right_depth == 0:
            return 1;
        elif left_depth != 0 and right_depth == 0:
            return 1 + left_depth;
        elif left_depth == 0 and right_depth != 0:
            return 1 + right_depth;
        else:
            return 1 + min(left_depth, right_depth);