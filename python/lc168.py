class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Get the ASCII number of a character
        # number = ord(char)

        # Get the character given by an ASCII number
        # char = chr(number)

        # similar to decimal /10 and %10
        
        i = 1;
        num_list = [];
        result = "";
        while 1:
            n = n - 1;
            #base = pow(26, i);
            base = 26
            quotient = n/base;
            remainder = n%base;

            # print "base: ", base
            # print quotient
            # print remainder

            num_list.append(remainder);

            n = n/base;
            # print "n", n
            if n == 0:
                break;
            
            i += 1;

        for i in range (0, len(num_list)):
            result = chr(ord('A') + num_list[i]) + result;


        
        return result;

