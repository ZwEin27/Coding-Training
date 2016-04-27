# http://bookshadow.com/weblog/2015/07/13/leetcode-lowest-common-ancestor-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# TLE
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pa, pb = self.find_path(root, p), self.find_path(root, q)
        size = min(len(pa), len(pb))
        # print pa
        # print pb
        idx = 0
        while idx < size:
            if pa[idx].val == pb[idx].val:
                idx += 1
            else:
                return pa[idx-1]

        return pa[idx-1]


    def find_path(self, root, target):
        stack = [root]
        visited = []
        ans = []
        while stack:
            node = stack[-1]
            if node.left and node.left not in visited:
                stack.append(node.left)
            elif node.right and node.right not in visited:
                stack.append(node.right)
            else:
                visited.append(node)
                if node.val == target.val:
                    # return stack
                    ans.append(list(stack))
                stack.pop(-1)
        return ans
