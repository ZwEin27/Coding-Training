# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True;
        else:
            if root.left == None and root.right == None:
                return True;
            elif root.left != None and root.right != None:
                return self.isMirror(root.left, root.right);
            else:
                return False;

    def isMirror(self, node1, node2):
        if node1 == None and node2 == None:
            return True;
        elif node1 != None and node2 != None:
            if node1.val == node2.val:
                return self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left);
            else:
                return False;
        else:
            return False;

        