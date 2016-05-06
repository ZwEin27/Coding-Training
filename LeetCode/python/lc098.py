# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True
        if not root.left and not root.right:
            return True

        nodes = []
        self.in_order_traversal(nodes, root)
        print nodes
        for i in range(1, len(nodes)):

            if nodes[i-1] >= nodes[i]:
                # print nodes[i-1], nodes[i] # -1, 0
                return False
        return True



    def in_order_traversal(self, nodes, node):
        if node.left:
            self.in_order_traversal(nodes, node.left)
        if node:
            nodes.append(node.val)
        if node.right:
            self.in_order_traversal(nodes, node.right)


if -1 >= 0:
    print 's'


    #     if not root:
    #         return True
    #     return self.dfs(root, None)
    #
    # def dfs(self, node, parent):
    #     if node.left:
    #         if parent:
    #             if node.val < parent.val:
    #                 if node.left.val >= parent.val:
    #                     return False
    #             if node.val > parent.val:
    #                 if node.left.val <= parent.val:
    #                     return False
    #         if node.val <= node.left.val:
    #             return False
    #         if not self.dfs(node.left, node):
    #             return False
    #
    #     if node.right:
    #         if parent:
    #             if node.val < parent.val:
    #                 if node.right.val >= parent.val:
    #                     return False
    #             if node.val > parent.val:
    #                 if node.right.val <= parent.val:
    #                     return False
    #         if node.val >= node.right.val:
    #             return False
    #         if not self.dfs(node.right, node):
    #             return False
    #     return True



        # stack = [root]
        # while stack:
        #     tmp = stack[-1]
        #     while tmp.left:
        #         tmp = tmp.left
        #         stack.append(tmp)
        #
        #     cur = stack.pop(-1)
        #     if cur.right:
        #         stack.append(cur.right)
