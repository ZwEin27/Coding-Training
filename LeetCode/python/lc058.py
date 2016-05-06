class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0;
        pre = 0;
        strlen = len(s);
        if strlen == 0:
            return 0;
        for i in range(0, strlen):
            count += 1;
            if s[i] == " ":
                count = 0;
            else:
                pre = count;
        if s[strlen - 1] == " ":
            return pre;
        return count;