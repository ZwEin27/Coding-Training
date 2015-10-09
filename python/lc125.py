# deal without goo performance
# need redesign this

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True;

        strlen = len(s);
        idx_start = 0;
        idx_end = strlen - 1;
        while idx_start < strlen:
            str_start = s[idx_start];
            str_end = s[idx_end];

            if self.needIgnore(str_start):
                idx_start += 1;
                continue;
            if self.needIgnore(str_end):
                idx_end -= 1;
                continue;

            if str_start.upper() == str_end.upper():
                idx_start += 1;
                idx_end -= 1;
            else:
                return False;

        if idx_start < strlen:
            return False;
        else:
            return True;

    def needIgnore(self, s):
        # if s == " " or s == "," or s == ":" or s == "." or s == "@" or :
        #     return True;
        # return False;

        tmp = ord(s);
        if tmp >= ord('0') and tmp <= ord('9'):
            return False;
        elif tmp >= ord('a') and tmp <= ord('z'):
            return False;
        elif tmp >= ord('A') and tmp <= ord('Z'):
            return False;
        else:
            return True;


