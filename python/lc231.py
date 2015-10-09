class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False;
        sbn = str(bin(n));
        sbn = sbn[2:];
        # print sbn
        for i in range(1, len(sbn)):
            # print sbn[i]
            if int(sbn[i]) != 0:
                return False;
        return True;
