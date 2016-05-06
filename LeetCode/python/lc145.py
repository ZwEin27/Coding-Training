# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # http://blog.csdn.net/hackbuteer1/article/details/6583988
        
        if root == None:
            return []

        stack_1 = [] # first in last out
        stack_2 = []
        result = []
        stack_1.append(root)
        # node = root
        while stack_1:
            node = stack_1.pop()
            stack_2.append(node)

            if node.left:
                stack_1.append(node.left)
            if node.right:
                stack_1.append(node.right)

        while stack_2:
            node = stack_2.pop()
            result.append(node.val)

        return result



        # while node == root or len(stack) != 0 or != 0 or node != None:
        #     #print result
        #     if node != None:
        #         stack.append(node)
        #         node = node.left
        #     else:
        #         if len(stack_right) != 0:
        #             node = stack_right.pop()
        #             result.append(node.val)
        #             if len(stack) != 0:
        #                 node = stack.pop()
        #                 stack_right.append(node)
        #                 node = node.right
        #             else:
        #                 node = None
        #         else:   
        #             node = stack.pop()
        #             stack_right.append(node)
                    
        #             node = node.right

        # return result




        """
        # recursive solution
        if root == None:
            return []
        result = []

        rel = self.postorderTraversal(root.left)
        if rel != None:
            result.extend(rel)

        rel = self.postorderTraversal(root.right)
        if rel != None:
            result.extend(rel)

        result.append(root.val)

        return result
        """