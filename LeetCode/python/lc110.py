# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True;

        if abs( self.maxDepth(root.left) - self.maxDepth(root.right) ) > 1 :
            return False;
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right);  # Notice, it's for two subtrees of any node

    def maxDepth(self, node):
        if node == None:
            return 0;        
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right));