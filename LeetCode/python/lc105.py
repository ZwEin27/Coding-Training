"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    """
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None
        root = TreeNode(preorder[0])
        root_pos = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:1+root_pos], inorder[:root_pos])
        root.right = self.buildTree(preorder[root_pos+1:], inorder[root_pos+1:])

        return root
    """

    def buildTree(self, preorder, inorder):
        if not inorder:
            return None
        if len(preorder) != len(inorder):
            return None
        return self.myTree(preorder, 0, len(preorder), inorder, 0, len(inorder))

    def myTree(self, preorder, pstart, pend, inorder, istart, iend):
        if istart >= iend:
            return None
        root = TreeNode(preorder[pstart])
        root_pos = inorder.index(root.val) - istart
        root.left = self.myTree(preorder, pstart+1, pstart+1+root_pos, inorder, istart, istart+root_pos)
        root.right = self.myTree(preorder, pstart+root_pos+1, pend, inorder,istart+root_pos+1, iend)

        return root




        
