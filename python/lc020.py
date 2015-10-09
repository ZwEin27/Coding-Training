#!/usr/bin/env python



class Solution:

    def __init__(self):  
        self.stack = [];
        self.size = 0;  

    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        for i in range(0, len(s)):
            cur = s[i];
            if cur == "(" or cur == "[" or cur == "{":
                self.push(cur);
            elif cur == ")":
                data = self.pop(cur);
                if data != "(":
                    return False;
            elif cur == "]":
                data = self.pop(cur);
                if data != "[":
                    return False;
            elif cur == "}":
                data = self.pop(cur);
                if data != "{":
                    return False;
            else:
                return False;
        if self.size == 0:
            return True;
        else:
            return False;

    def push(self, s):
        self.stack.append(s);
        self.size += 1;

    def pop(self, s):
        if self.size <= 0:
            return "error";
        data = self.stack[-1];
        del self.stack[-1];
        self.size -= 1;
        return data;
        