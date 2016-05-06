# http://bookshadow.com/weblog/2015/08/13/segment-tree-set-1-sum-of-given-range/
# http://bookshadow.com/weblog/2015/11/18/leetcode-range-sum-query-mutable/


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        pass

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        pass

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        pass

    def lowbit(sef, x):
        return x & -x

        
nums = [1, 3, 5]

# Your NumArray object will be instantiated and called as such:
numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# print numArray.sumRange(1, 2)


for i in range(100):
    print str(i) + ":  " + str(numArray.lowbit(i))




## Time excceed

"""
class NumArray(object):
    def __init__(self, nums):
        self.nums_size = len(nums)
        self.nums = nums
        self.changes = {}
        # self.changes = [0] * (self.nums_size)
        self.sum_list = [0] * (self.nums_size+1)
        for i in range(self.nums_size):
            self.sum_list[i+1] = self.nums[i] + self.sum_list[i]

        

    def update(self, i, val):
        # self.nums[i] = val
        # for j in range(i, self.nums_size):
        #     self.sum_list[j+1] = self.nums[j] + self.sum_list[j]
        #     
        self.changes.setdefault(i, val)
        self.changes[i] = val - self.nums[i]
        # self.changes[i] = val - self.nums[i]


    def sumRange(self, i, j):
        diff = 0
        for (k, v) in self.changes.items():
            if k >= i and k <= j:
                diff += self.changes[k]
        return self.sum_list[j+1] - self.sum_list[i+1] + self.nums[i] + diff

"""