
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return math.sqrt(n) if n > 0 else 0


        """ memory limit exceeded 
        if n <= 0:
            return 0
        if n == 1 or n == 2 or n == 3:
            return 1

        # n > 3
        total = 1
        for i in range(4, n+1):
            if not (i%2 == 0 or i%3 == 0):
                total += 1

        if n%2 == 0:
            return total+1
        else:
            return total-1
        """


        """ memory limit exceeded 
        if n <= 0:
            return 0

        if n >= 1:
            bulbs = [1]*n
        if n >= 2:
            for i in range(1, n+1):
                if i%2 == 0:
                    bulbs[i-1] = 0
        if n >= 3:
            for i in range(1, n+1):
                if i%3 == 0:
                    tmp = bulbs[i-1]
                    bulbs[i-1] = 1 if tmp == 0 else 0

        for i in range(3, n):
            bulbs[-1] = 1 if tmp == 0 else 0

        on_bulbs = 0
        for i in range(n):
            on_bulbs += 1 if bulbs[i] == 1 else 0

        return on_bulbs
        """


# print Solution().bulbSwitch(7)

