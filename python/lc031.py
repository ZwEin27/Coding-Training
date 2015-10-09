class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # http://blog.csdn.net/lanxu_yy/article/details/17593937
        
        nlen = len(nums)

        if nlen > 1:
            i = nlen -1
            while i > 0:
                if nums[i-1] < nums[i]:
                    break
                i -= 1
            if i == 0:
                # nums.sort()
                for k in range(0, nlen/2):
                    self.swap(nums, k, nlen-1-k);  
            else:
                ii = i
                i = i - 1
                j = nlen - 1
                while j >= 0:
                    if nums[j] > nums[i]:
                        break
                    j -= 1
                self.swap(nums, j, i)


                for k in range(0, (nlen - ii)/2):
                    self.swap(nums, ii+k, nlen-1-k);  



        # print nums


        
    def swap(self, nums, p, q):
        tmp = nums[p]
        nums[p] = nums[q]
        nums[q] = tmp

