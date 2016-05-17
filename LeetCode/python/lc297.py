# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '{}'
        queue = [root]
        ans = []
        while queue:
            node = queue.pop(0)
            if node:
                ans.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                ans.append('#')

        while ans[-1] == '#':
            ans.pop()

        return '{' + ','.join(ans) + '}'


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '{}':
            return None
        data = data[1:-1]
        data = data.split(',')
        root = TreeNode(data[0])
        queue = [root]
        isLeft = True
        index = 0
        for i in range(1, len(data)):
            node = TreeNode(data[i])
            if node.val != '#':
                if isLeft:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)
            if not isLeft:
                index += 1
            isLeft = not isLeft
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
