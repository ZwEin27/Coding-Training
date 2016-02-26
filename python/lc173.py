# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# double stack
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack_a = []
        self.stack_b = []
        if root:
            self.stack_a.append(root)

        # while self.stack:
        #     cur_node = self.stack.pop(-1)
        #     if cur_node.right:
        #         self.stack.append(cur_node.right)
        #     self.stack.append(cur_node)
        #     if cur_node.left:
        #         self.stack.append(cur_node.left) 



    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack_a or self.stack_b:
            return True
        return False

    def next(self):
        """
        :rtype: int
        """
        while self.stack_a:
            cur_node = self.stack_a.pop(-1)
            self.stack_b.append(cur_node)
            if cur_node.left:
                self.stack_a.append(cur_node.left)
        next_node = self.stack_b.pop(-1)
        if next_node.right:
            self.stack_a.append(next_node.right)
        return next_node.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
