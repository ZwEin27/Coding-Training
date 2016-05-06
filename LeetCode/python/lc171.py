class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        slen = len(s);
        power = 0;
        result = 0;
        for i in range(0, slen):
            ch = s[i];
            num = ord(ch) - ord('A') + 1;
            print num
            result = result*26;
            result += num;
        return result;