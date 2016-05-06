# http://blog.csdn.net/ljiabin/article/details/45846837
# http://www.cnblogs.com/easonliu/p/4483437.html

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
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
        while queue:
            cur = queue.pop(0)
            k += 1
            for i in oud[cur]:
                ind[i] -= 1
                if ind[i] == 0:
                    queue.append(i)
        return k == numCourses




numCourses = 3
prerequisites = [[1,0],[0,1]]

print Solution().canFinish(numCourses, prerequisites)




""" TLE

ht = {}
        for p in prerequisites:
            ht.setdefault(p[0], [])
            ht[p[0]].append(p[1])

        

        for node in ht:
            stack = []
            isVisited = [0] * numCourses
            stack.append(node)

            while stack:
                cur = stack.pop(-1)
                # print cur
                if isVisited[cur] != 0:
                    return False

                isVisited[cur] = 1
                nexts = ht.get(cur, [])
                for n in nexts:
                    stack.append(n)

        return True

"""