# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.buildTree(0, n)


    def buildTree(self, begin, end):
        tree_list = []
        if begin >= end:
            tree_list.append(None)
            return tree_list

        for i in range(begin, end):
            lefts = self.buildTree(begin, i)
            rights = self.buildTree(i+1, end)

            for j in range(len(lefts)): 
                left = lefts[j]
                for k in range(len(rights)):
                    right = rights[k]
                    tree = TreeNode(i+1) 
                    tree.left = left
                    tree.right = right
                    tree_list.append(tree)

        return tree_list

