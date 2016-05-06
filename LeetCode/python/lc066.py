class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dlen = len(digits);
        flag = 0;
        for i in range(0, dlen):
            idx = dlen - 1 - i;
            digit = digits[dlen - 1 - i];
            if i == 0:
                digit += 1;
            if flag == 1:
                digit += 1;
                flag = 0;
            
            digits[idx] = digit;
            if digit >= 10:
                flag = 1;
                digits[idx] = 0;
                if i == dlen - 1:
                    digits.insert(0, 1);
            
        return digits;