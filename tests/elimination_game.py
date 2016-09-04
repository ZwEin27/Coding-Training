class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        nums = [_ for _ in range(2, n+1, 2)]
        flag = 1
        while len(nums) > 1:
            if flag == 0:
                size = len(nums)/2 if len(nums) % 2 == 0 else len(nums)/2 + 1
                for i in range(size):
                    del nums[i]
                flag = 1
            else:
                if len(nums) % 2 == 0:
                    for i in range(1, len(nums)/2):
                        del nums[i]
                else:
                    for i in range(0, len(nums)/2+1):
                        del nums[i]

                flag = 0

        return nums[0]

print Solution().lastRemaining(4)


"""
class Solution(object):
    def lastRemaining(self, n):
        if n == 1:
            return n
        nums = [_ for _ in range(2, n+1, 2)]
        flag = 1
        while len(nums) > 1:

            if flag == 0:
                nums = [nums[_] for _ in range(1, len(nums), 2)]
                flag = 1
            else:
                if len(nums) % 2 == 0:
                    nums = [nums[_] for _ in range(0, len(nums), 2)]
                else:
                    nums = [nums[_] for _ in range(1, len(nums), 2)]
                # nums = [nums[_] for _ in range(len(nums)-2, -1, -2)][::-1]
                flag = 0
            # print nums

        return nums[0]
"""
