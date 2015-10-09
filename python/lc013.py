#!/usr/bin/env python

# 1~9: {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};

# 10~90: {"X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};

# 100~900: {"C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};

# 1000~3000: {"M", "MM", "MMM"}.


class Solution:

    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        string = str(s);
        strlen = len(string);
        result = 0;
        cur = 0;
        pre = 0;
        for i in range(0, strlen): 
            cur = self.SymboltoNumber(string[i]);
            # MMMCMXCIX
            # 3000 + 100 = 3100
            # 3000 + 1000 - 100 - 100

            if pre < cur:
                result = result + cur - 2*pre;
            else:
                result = result + cur;
            pre = cur;
        return result;

    def SymboltoNumber(self, s):
        if s == "I":
            return 1;
        elif s == "V":
            return 5;
        elif s == "X":
            return 10;
        elif s == "L":
            return 50;
        elif s == "C":
            return 100;
        elif s == "D":
            return 500;
        elif s == "M":
            return 1000;
        else:
            return 0;

        