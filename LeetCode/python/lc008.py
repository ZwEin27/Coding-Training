#!/usr/bin/env python

# Implement atoi to convert a string to an integer.

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        result = 0;
        strlen = len(str);
        if strlen == 0:
            return 0;

        startIdx = 0;
        blankflag = 0;
        for i in range(0, strlen):
            tmp = str[i];
            if ord(tmp) >= ord('0') and ord(tmp) <= ord('9'):
                blankflag = 1;
                result = 10*result + ord(tmp) - ord('0');
            elif tmp == "+" or tmp == "-":
                blankflag = 1;
                if i != startIdx:
                    return 0;
                else:
                    continue;
            elif tmp == " ":
                if blankflag == 1:
                    break;
                startIdx = startIdx + 1;  
                continue;
            else:
                break;

        

        
        if str[startIdx] == "-":
            result = - result;

        maxInt = 2147483647;
        minInt = -2147483648;
        if result > maxInt:
            result = maxInt;
        if result < minInt:
            result = minInt;

        return result;

        