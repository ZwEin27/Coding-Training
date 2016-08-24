class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        combinations = self.combination(k)
        for c in combinations:
            if sum(c) == n:
                ans.append(c)
        return ans


    def combination(self, k):
        ans = []
        self.search([], k, 1, 9, ans)
        return ans

    def search(self, alist, k, start, end, ans):
        if len(alist) == k:
            ans.append(alist)
            return

        for num in range(start, end+1):
            # if num not in alist:
            self.search(alist+[num], k, num+1, end, ans)
        
