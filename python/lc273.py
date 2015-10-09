class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        result = ""
        
        step_str = ["", "Thousand", "Million", "Billion"]

        step = 0
        while num > 0:
            # print num
            tmp = self.helper(num % 1000)

            if tmp != "":
                if step != 0:
                    tmp += " " + step_str[step]
                else:
                    tmp += step_str[step]

            if result != "":
                if tmp != "":
                    result = tmp + " " + result
            else:
                result = tmp + result
            # result = self.helper(num % 1000) + step_str[step] + result
            num /= 1000
            step += 1

        return result

    def helper(self, num):
        # process three digits
        # print num
        result = ""
        digits_str_1 = ["Unused", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        digits_str_2 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        digits_str_3 = ["Unused", "Unused", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        hundred = num/100
        ten = num%100/10
        digit = num%10

        # print ten

        if hundred != 0:
            result += digits_str_1[hundred] + " Hundred"

        if ten != 0:
            if hundred != 0:
                result += " "
            if ten == 1:
                result += digits_str_2[digit]
                return result
            else:
                result += digits_str_3[ten]

        if digit != 0:
            if hundred != 0 or ten != 0:
                result += " "
            
            result += digits_str_1[digit]

        return result









