class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [1]*n;

        i = 2;
        while i*i < n:
            if not isPrime[i]:
                continue;
            j = i*i;
            while j < n:
                isPrime[j] = 0;
                j += i;
            i += 1;

        count = 0;
        for i in range(2, n):
            if isPrime[i]:
                count += 1;
        return count;