class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numlist = [];
        tmp = n;
        while 1:
            tmp = self.sd(tmp);
            if tmp == 1:
                return True;
            else:
                if tmp in numlist:
                    return False;
                else:
                    numlist.append(tmp);

    def sd(self, num):
        numstr = str(num);
        numlen = len(numstr);
        result = 0;
        for i in range(0, numlen):
            result += pow(int(numstr[i]), 2);
        return result;
