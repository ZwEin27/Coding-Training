# http://www.tuicool.com/articles/NVNbMj

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        ind = [0] * numCourses  # indegree
        oud = [[] for _ in xrange(numCourses)]  # outdegree

        for p in prerequisites:
            ind[p[1]] += 1
            oud[p[0]].append(p[1])

        queue = []

        for i in range(numCourses):
            if ind[i] == 0:
                queue.append(i)

        k = 0
        ans = []
        while queue:
            cur = queue.pop(0)
            ans = [cur] + ans
            k += 1
            for i in oud[cur]:
                ind[i] -= 1
                if ind[i] == 0:
                    queue.append(i)
        if k == numCourses:
            return ans
        return []

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print Solution().findOrder(numCourses, prerequisites)