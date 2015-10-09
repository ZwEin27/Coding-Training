# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        outer_list = [];
        

        node = root;
        if node == None:
            return outer_list;

        q1 = [];
        q1.append(node);

        while len(q1) != 0:     # Node, cannot use != None
            q2 = [];
            inner_list = [];
            while len(q1) != 0:
                node = q1.pop(0);
                inner_list.append(node.val);
                if node.left != None:
                    q2.append(node.left);
                if node.right != None:
                    q2.append(node.right);
            q1 = q2;
            outer_list.append(inner_list);

        outer_list.reverse();
        return outer_list;