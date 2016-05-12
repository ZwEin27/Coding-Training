"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        maxPath, _ = self.search(root)
        return maxPath

    def search(self, root):
        if not root:
            return -sys.maxint, 0

        left = self.search(root.left)
        right = self.search(root.right)

        maxPath = max(left[0], right[0], root.val + left[1] + right[1])
        single = max(root.val + left[1], root.val + right[1], 0) # here is 0, not root.val

        return maxPath, single

        
