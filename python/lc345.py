class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        import re
        vowels = re.findall('[aeiouAEIOU]', s)
        # print vowels
        return re.sub('[aeiouAEIOU]', lambda m: vowels.pop(-1), s)

s = 'Aa'
print Solution().reverseVowels(s)
