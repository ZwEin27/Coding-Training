
# http://blog.csdn.net/ciaoliang/article/details/50791254

class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        xlen = len(x)
        for i in range(xlen):
            if i >= 3 and x[i] >= x[i-2] and x[i-3] >= x[i-1]:
                return True
            if i >= 4 and x[i-1] == x[i-3] and x[i] + x[i-4] >= x[i-2]:
                return True
            if i >= 5 and x[i-3] >= x[i-1] and x[i-2] >= x[i-4] and x[i] + x[i-4] >= x[i-2] and x[i-1] + x[i-5] >= x[i-3]:
                return True


        return False

x = [1,1,2,1,1]
print Solution().isSelfCrossing(x)
