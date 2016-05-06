class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return Integer.MAX_INT

        maxint = (1<<31) -1
        minint = -(1<<31)
        # print minint
        res = 0
        # if dividend > maxint:
        #     dividend = maxint


        if min(dividend, divisor) < 0 and max(dividend, divisor) > 0:
            isNeg = True
        else:
            isNeg = False

        dividend = abs(dividend)
        divisor = abs(divisor)

        digit = 0
        
        while divisor <= (dividend >> 1) :
            divisor <<= 1
            digit += 1

        while digit >= 0:
            if dividend >= divisor:
                dividend -= divisor
                res += 1 << digit
            divisor >>= 1
            digit -= 1

   
        # print res
        if isNeg:
            if -res < minint:
                return minint
            else:
                return -res
        else:
            if res > maxint:
                return maxint
            else:
                return res

       