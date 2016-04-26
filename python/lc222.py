# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        tmp = root
        height = 0
        while tmp.left:
            tmp = tmp.left
            height += 1

        left = 0
        right = pow(2, height) - 1

        while left <= right:
            mid = (left + right) / 2
            if self.get_node(root, mid, height):
                left = mid + 1
            else:
                right = mid - 1
        total = 0
        for i in range(height):
            total += 1 << i
        return total + right + 1

    def get_node(self, root, idx, height):
        node = root
        while height:
            height -= 1
            if idx & 1 << height:
                node = node.right
            else:
                node = node.left
        return node
