# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = [];
        if root != None:
            if root.left != None:
                val_left = self.binaryTreePaths(root.left);
                for i in range(len(val_left)):
                    result.append(str(root.val) + "->" + val_left[i]);
            if root.right != None:
                val_right = self.binaryTreePaths(root.right);
                for i in range(len(val_right)):
                    result.append(str(root.val) + "->" + val_right[i]);
            if root.left == None and root.right == None:
                result.append(str(root.val));
        return result;