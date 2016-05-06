# https://leetcode.com/discuss/71763/share-some-thoughts
# http://bookshadow.com/weblog/2015/11/26/leetcode-minimum-height-trees/

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        ht = {_:[] for _ in range(n)}

        for s,t in edges:
            ht[s].append(t)
            ht[t].append(s)

        leaves = [ x for x in range(n) if len(ht[x]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leave in leaves:
                for parent in ht[leave]:
                    ht[parent].remove(leave)
                    if len(ht[parent]) == 1:
                        new_leaves.append(parent)
            leaves = new_leaves
        return leaves

        # for node in ht:
        #     queue = [(node, 0)]
        #     visited = []
        #     while queue:
        #         cur, level = queue.pop(0)
        #         visited.append(cur)
        #         levels[node] = max(levels[node], level)
        #         for i in ht[cur]:
        #             if i not in visited:
        #                 queue.append((i, level+1))








n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print Solution().findMinHeightTrees(n, edges)




""" TLE

        ht = {_:[] for _ in range(n)}
        levels = [0] * n
        for edge in edges:
            ht[edge[0]].append(edge[1])
            ht[edge[1]].append(edge[0])

        for node in ht:
            queue = [(node, 0)]
            visited = []
            while queue:
                cur, level = queue.pop(0)
                visited.append(cur)
                levels[node] = max(levels[node], level)
                for i in ht[cur]:
                    if i not in visited:
                        queue.append((i, level+1))

        ans = []
        min_level = min(levels)
        for i in range(n):
            if levels[i] == min_level:
                ans.append(i)

        return ans
"""


