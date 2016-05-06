#!/usr/bin/env python

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return "";
        idx = 0;
        result = "";
        firstStr = strs[0];
        for idx in range(0, len(firstStr)):
            tmp = firstStr[idx];
            for i in range(1, len(strs)):
                string = strs[i];
                if idx >= len(string):
                    return result;
                if tmp != string[idx]:
                    return result;
            result += tmp;

        return result;
        