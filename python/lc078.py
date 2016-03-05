class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        size = len(nums)
        # result = self.combination(1, size, 0)
        result = []
        for i in range(0, size+1):
            result.extend(self.combination(nums, 0, size, i)) 
        return result

    def combination(self, nums, start, end, k):
        ans = []
        if k >= 2:
            for i in range(start, end): # 1,2,3 - 3 times
                rels = self.combination(nums, i+1, end, k-1)
                for rel in rels:
                    tmp = [nums[i]]
                    tmp.extend(rel)
                    ans.append(tmp)
        elif k == 1:
            for i in range(start, end):
                ans.append([nums[i]])
        else:
            ans.append([])
        
        return ans

if __name__ == '__main__':
    s = Solution()
    print s.subsets([4,1,0])