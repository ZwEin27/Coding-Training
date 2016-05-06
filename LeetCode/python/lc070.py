class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        

        if n <= 2:
            return n;
        # time exceed by using this method.
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2);
        pre = 1;
        cur = 1;
        for i in range(1, n):
            tmp = pre + cur;
            pre = cur;
            cur = tmp;
        return cur;

        # 1 1 2 3 5
