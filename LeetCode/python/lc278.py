# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # http://www.cnblogs.com/grandyang/p/4790469.html

        left = 1
        right = n

        while left < right:
            mid = left + (right - left) / 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

    #     return self.badVersion(1, n)


    # def badVersion(self, begin, end):
    #     nlen = end - begin + 1

    #     if begin == end:
    #         return begin

    #     if nlen % 2 == 0:
    #         mid = nlen/2
    #     else:
    #         mid = nlen/2 + 1

    #     step = mid/2
    #     if isBadVersion(begin + mid - 1):
    #         rel = self.badVersion(begin, begin + step)
    #     else:
    #         rel = self.badVersion(end - step, end)

    #     return rel





        