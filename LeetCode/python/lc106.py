"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    """
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None

        root = TreeNode(postorder[-1])
        root_pos = inorder.index(root.val)

        root.left = self.buildTree(inorder[:root_pos], postorder[:root_pos])
        root.right = self.buildTree(inorder[1+root_pos:], postorder[root_pos:-1])
        return root
    """

    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        if len(inorder) != len(postorder):
            return None
        return self.myTree(inorder, 0, len(inorder), postorder, 0, len(postorder))

    def myTree(self, inorder, istart, iend, postorder, pstart, pend):
        if istart >= iend:
            return None
        root = TreeNode(postorder[pend-1])
        root_pos = inorder.index(root.val) - istart
        root.left = self.myTree(inorder, istart, istart+root_pos, postorder, pstart, pstart+root_pos)
        root.right = self.myTree(inorder, istart+root_pos+1, iend, postorder, pstart+root_pos, pend-1)
        return root
