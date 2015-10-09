class Solution(object):
    # def __init__(self):
    #     self.maxpslen = 0
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """        

        # need try again with manacher algorithm
        slen = len(s)
        longest = ""

        for i in range(slen):
            tmp = self.isPalindrome(s, i, i)
            if len(tmp) > len(longest):
                longest = tmp

            tmp = self.isPalindrome(s, i, i+1)
            if len(tmp) > len(longest):
                longest = tmp
        return longest


    def isPalindrome(self, s, start, end):
        slen = len(s)

        while 0 <= start and end <= slen - 1:
            if s[start] == s[end]:
                start -= 1
                end += 1
            else:
                break
        # start reduce one more time
        # end doesn't include, it's [)
        return s[start+1:end]
        # cadacm
