class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        # time exceed 

        n1len = len(num1)
        n2len = len(num2)

        if n1len == 0 or n2len == 0:
            return "0"

        
        # idx_big = n2len - 1
        if n1len >= n2len:
            num_big = num1
            num_small = num2
            idx_small = n2len - 1
        else:
            num_small = num1
            num_big = num2
            idx_small = n1len - 1

        result = "0"
        
        step = 0
        while idx_small >= 0:


            digit = num_small[idx_small]
            #print pow(10, step)
            ans = self.mul(num_big, digit)
            #print ans
            for i in range(step):
                ans += "0"

            #print ans
            result = self.add(result, ans)
            #print result
            idx_small -= 1
            step += 1
        return result

    def add(self, num1, num2):
        
        return str(int(num1) + int(num2))

        # n1len = len(num1)
        # n2len = len(num2)

        # n1idx = n1len - 1
        # n2idx = n2len - 1

        # result = ""
        # tens = 0
        # while n1idx >= 0 and n2idx >= 0:
        #     tmp = int(num1[n1idx]) + int(num2[n2idx]) + tens
        #     bits = tmp%10

        #     result = str(bits) + result
        #     tens = tmp/10
        #     n1idx -= 1
        #     n2idx -= 1

        # # print result

        # if n1idx >= 0:
        #     while n1idx >= 0:
        #         tmp = int(num1[n1idx]) + tens
        #         bits = tmp%10

        #         result = str(bits) + result
        #         tens = tmp/10
        #         n1idx -= 1
        #     # if tens != 0:
        #     #     result = str(tens) + result

        # if n2idx >= 0:
        #     while n2idx >= 0:
        #         tmp = int(num2[n2idx]) + tens
        #         bits = tmp%10

        #         result = str(bits) + result
        #         tens = tmp/10
        #         n2idx -= 1

        # if tens != 0:
        #     result = str(tens) + result

        # return result

    def mul(self, num, digit):
        nlen = len(num)
        if digit == 0:
            return 0

        result = ""
        tens = 0
        i = nlen - 1
        while i >= 0:
            tmp = int(num[i]) * int(digit) + tens
            bits = tmp%10

            result = str(bits) + result
            tens = tmp/10

            i -= 1
        if tens != 0:
            result = str(tens) + result

        return result

