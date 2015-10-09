class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        bitstr = bin(n);
        bitstr = bitstr[2:];
        count = 0;
        for i in range(0, len(bitstr)):
            if 1 == int(bitstr[i]):
                count += 1;
        return count;
        """

        # http://www.tuicool.com/articles/YBbY3m
        
        count = 0;
        while n:
            count += 1;
            n = n&(n-1);
        return count