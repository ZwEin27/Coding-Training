#!/usr/bin/env python


class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        strInt = str(x);
        strLen = len(strInt);
        for i in range(0, strLen):
            if strInt[i] != strInt[strLen - i - 1]:
                return False;

        return True;