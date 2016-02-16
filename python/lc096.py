
# http://www.cnphp6.com/archives/61820?utm_source=tuicool&utm_medium=referral

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        uniqueTrees = {}
        uniqueTrees.setdefault(0, 1)
        uniqueTrees.setdefault(1, 1)

        for i in range(2, n+1):
            uniqueTrees.setdefault(i, 0)
            for k in range(i):
                uniqueTrees[i] += uniqueTrees[k] * uniqueTrees[i-k-1]
        return uniqueTrees[n] 



        # uniqueTrees={}
        # uniqueTrees[0] = 1
        # uniqueTrees[1] = 1
 
        # for cnt in range(2, n+1):
        #     uniqueTrees[cnt] = 0
        #     for k in range(0, cnt):
        #         uniqueTrees[cnt] += uniqueTrees[k]*uniqueTrees[cnt-1-k]

        # return uniqueTrees[n]
