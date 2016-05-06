# https://leetcode.com/discuss/88125/python-easy-to-understand-solution

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})
    
    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []
    
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res




s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print Solution().wordBreak(s, wordDict)


""" TIME LIMIT EXCCEED

str_size = len(s)
        result = []
        for i in range(1, str_size+1):
            string = s[:i]
            if string in wordDict:
                if i < str_size:

                    wlist = self.wordBreak(s[i:], wordDict)
                    for w in wlist:
                        result.append(string + ' ' + w)
                else:
                    result.append(string)
        return result


"""
