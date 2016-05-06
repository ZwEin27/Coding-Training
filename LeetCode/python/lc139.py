# http://www.tuicool.com/articles/Iv2QJf

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        size = len(s)
        dp = [False] * (size + 1)
        dp[0] = True

        for i in range(1, size + 1):
            # print 'i: ' + s[:i]
            for j in range(0, i):
                # print s[j:i]
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[size]


        



s = "aaaaaaa"
wordDict = ["aaaa","aaa"]
print Solution().wordBreak(s, wordDict)




""" TIME LIMIT EXCCEED
class Solution(object):
    def wordBreak(self, s, wordDict):
        str_size = len(s)
        for i in range(1, str_size+1):
            string = s[:i]
            if string in wordDict:
                if i < str_size:
                    if self.wordBreak(s[i:], wordDict):
                        return True
                else:
                    return True
        return False

"""