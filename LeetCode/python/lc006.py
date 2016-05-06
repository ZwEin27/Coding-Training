#!/usr/bin/env python

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        result = "";
        numMid = numRows - 2;
        zipSpan = numMid + numRows;     # zipSpan = numRows*2 - 2
        strlen = len(s);
        #result = s[0+numRows+numMid];
        for i in range(0, numRows):
            if numRows == 1:
                result = s;
                return result;
            for j in range(0,strlen):
                if i == 0 or i == numRows - 1:
                    idx = i + j*zipSpan;
                else:
                    if j%2 == 0:
                        idx = i + (j/2)*zipSpan;
                    else:
                        idx = i + (j/2+1)*zipSpan - 2*i;

                if idx>=strlen:
                    break;

                result = result + s[idx];

        return result;



