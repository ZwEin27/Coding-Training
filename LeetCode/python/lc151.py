class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        string = s.split(' ')
        result = ''

        for word in string:
            if len(word) > 0:
                if len(result) > 0:
                    result = ' ' + result
                result = word + result
        # print result
        return result

        



s = "1 "
Solution().reverseWords(s)
