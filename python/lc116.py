# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        # http://www.cnblogs.com/felixfang/p/3647898.html
        if root == None:
            return None

        while root.left != None:    # use current layer to set next layer
            cur = root
            while cur != None:
                cur.left.next = cur.right
                if cur.next != None:
                    cur.right.next = cur.next.left
                cur = cur.next
            root = root.left
