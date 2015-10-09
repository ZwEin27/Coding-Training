# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.sum = 0;

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False;
        self.sum = sum;
        return self.sumPath(root, 0);

    def sumPath(self, node, pre_val):
        tmp = node.val + pre_val;
        result = False;

        if node.left != None:
            result = result or self.sumPath(node.left, tmp);
        if node.right != None:
            result = result or self.sumPath(node.right, tmp);

        if node.left == None and node.right == None and tmp == self.sum:
            return True;

        return result;


        