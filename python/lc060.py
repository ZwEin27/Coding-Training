# https://leetcode.com/discuss/75515/44ms-python-solution
# http://blog.csdn.net/doc_sgl/article/details/12840715

from math import factorial  
class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        nums = [i for i in xrange(1, n+1)]
        while n-1 >= 0:
            num, k = k/factorial(n-1), k % factorial(n-1)
            if k > 0:
                res.append(str(nums[num]))
                nums.remove(nums[num])
            else:
                res.append(str(nums[num-1]))
                nums.remove(nums[num-1])

            n -= 1

        return ''.join(res)


n = 3
k = 2
print Solution().getPermutation(n, k)



"""TLS

def getPermutation(self, n, k):
        
        nums = [i for i in range(1, n+1)] 
        # print nums
        res = [] 
        for i in range(1, n+1):
            self.permutation_sequence(i, list(nums), '', res)
        return res
    def permutation_sequence(self, idx, nums, path, res):
        nums.remove(idx)
        if not nums:
            path += str(idx)
            res.append(path)
        
        path += str(idx)
        if nums:
            # print 'path: ' + path
            
            for num in nums:
                # print 'num' + str(num)
                # print 'nums'
                # print nums
                self.permutation_sequence(num, list(nums), path, res)
"""
