# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        result = {}
        queue = []
        queue.append((root, 0))

        while len(queue) > 0:
            cur, level = queue.pop(0)
            result.setdefault(level, 0)
            result[level] = cur.val
            if cur.left:
                queue.append((cur.left, level+1))
            if cur.right:
                queue.append((cur.right, level+1))
        return result.values()
