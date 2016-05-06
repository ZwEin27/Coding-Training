# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None:
            return []
        stack = [] # first in last out
        result = []
        # stack.append(root)
        node = root

        while node == root or len(stack) != 0 or node != None:
            #print result
            if node != None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right

        return result




        

        """
        # recursive solution
        if root == None:
            return []
        result = []

        rel = self.inorderTraversal(root.left)
        if rel != None:
            result.extend(rel)

        result.append(root.val)

        rel = self.inorderTraversal(root.right)
        if rel != None:
            result.extend(rel)



        return result
        """