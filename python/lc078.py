class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        return self.combination(1, size, 2)

    def combination(self, start, end, k):
        ans = []
        if k >= 2:
            for i in range(start, end): # 1,2,3 - 3 times
                rels = self.combination(i+1, end, k-1)
                for rel in rels:
                    tmp = [i]
                    tmp.extend(rel)
                    ans.append(tmp)
        else:
            for i in range(start, end+1):
                ans.append([i])
        return ans

if __name__ == '__main__':
    s = Solution()
    print s.subsets([1,2,3])