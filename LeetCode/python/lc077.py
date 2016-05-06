class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.combination(1, n, k)    # deal with 1 to n

    def combination(self, start, end, k):
        ans = []
        if k >= 2:
            for i in range(start, end): # loop start to end times. e.g.  1-4, we need [1, x] [2, x] [3, x], three times needed
                rels = self.combination(i+1, end, k-1)  # current have i, recursively add one more, e.g. k=2, next get [[2],[3],[4]] for i = 1
                for rel in rels:
                    tmp = [i]
                    tmp.extend(rel)
                    ans.append(tmp)
        else:
            for i in range(start, end+1):
                ans.append([i])
        return ans

        






"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    The code below is for test only, please ignore it before submission

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
if __name__ == '__main__':
    s = Solution()
    print s.combine(5, 3)
