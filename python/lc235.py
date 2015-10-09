# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None

        rel_left = self.lowestCommonAncestor(root.left, p, q)
        rel_right = self.lowestCommonAncestor(root.right, p, q)

        if root == p or root == q:
            return root

        if rel_left != None and rel_right != None:
            return root

        if rel_left != None and rel_right == None:
            if rel_left != p or rel_left != q:
                return rel_left
            if (rel_left == p or rel_left == q) and (root == p or root == q) : 
                return root

        if rel_right != None and rel_left == None:
            if rel_right != p or rel_right != q:
                return rel_right
            if (rel_right == p or rel_right == q) and (root == p or root == q) : 
                return root
        
        return None



        