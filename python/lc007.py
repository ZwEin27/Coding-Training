#!/usr/bin/env python

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        result = "";
        if x<0:
            result += "-";
            x = -x;

        if x >= pow(2,31):
            return 0;

        strInt = str(x);
        strlen = len(strInt);

        if strlen == 1:
            return int(result + strInt);

        flag = 0;
        for i in range(0,strlen):
            tmp = strInt[strlen - i - 1];
            if tmp == "0" and flag == 0:
                continue;
            else:
                flag = 1;
            result = result + tmp;

        if abs(int(result)) >= pow(2,31):
            return 0;
        return int(result);
