# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None

        import math
        queue = [(root,0)]
        ans = []

        while queue:
            node, level = queue.pop(0)
            if len(ans) < level:
                ans.append([])


            if level % 2 == 0:
                ans[level].append(node.val)
            else:
                ans[level].insert(0, node.val)

            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return ans

ans = []
ans.append([])
print ans
