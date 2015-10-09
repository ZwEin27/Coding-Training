class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = ""
        if (numerator<0 and denominator>0) or (numerator>0 and denominator<0):
            result += '-';

        numerator = abs(numerator)
        denominator = abs(denominator)

        quotient = numerator/denominator
        remainder = numerator%denominator

        result += str(quotient)
        
        if remainder == 0:
            return result
        else:
            # numerator < denominator
            result += "."

        ht = {}

        while remainder:
            if ht.has_key(remainder):
                pos = ht[remainder]
                print pos
                result = result[:pos] + "(" + result[pos:] + ")"

                #result += "(" + str(remainder) + ")"
                break

            ht[remainder] = len(result)

            remainder *= 10
            result += str(remainder/denominator)


            remainder = remainder % denominator



        return result





        
