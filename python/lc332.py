# https://leetcode.com/discuss/84659/short-ruby-python-java-c

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # import collections
        # targets = collections.defaultdict(list)

        targets = {}

        for a, b in sorted(tickets):#[::-1]:
            targets.setdefault(a, [])
            targets[a].append(str(b))

            # targets[a] += b,

        route = []
        def visit(start):
            # while targets[start]:
            while start in targets.keys() and len(targets[start]) > 0:
                end = targets[start].pop(0)
                visit(end)
            route.append(start)
        visit('JFK')
        return route[::-1]

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# ["JFK", "MUC", "LHR", "SFO", "SJC"].
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print Solution().findItinerary(tickets)


"""

        ans = []
        self.dfs(tickets, 'JFK', ['JFK'], ans)

        return ans


    def dfs(self, tickets, target, itinerary, ans):
        if not tickets:
            ans.append(itinerary)
            return

        for i in range(len(tickets)):
            if tickets[i][0] == target:
                ci = list(itinerary)
                ci.append(tickets[i][1])
                ct = list(tickets)
                del ct[i]
                self.dfs(ct, tickets[i][1], ci, ans)

"""
