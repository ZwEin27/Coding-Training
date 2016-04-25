# http://bookshadow.com/weblog/2015/08/10/leetcode-clone-graph/

# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        stack = [node]
        cloned_graph_root = UndirectedGraphNode(node.label)
        ht = {node.label:cloned_graph_root}
        cloned_nodes = []
        while stack:
            node = stack.pop()
            cnode = ht[node.label]
            for nei in node.neighbors:
                if nei.label not in ht.keys():
                    ht[nei.label] = UndirectedGraphNode(nei.label)
                    stack.append(nei)
                cnode.neighbors.append(ht[nei.label])
        return cloned_graph_root
