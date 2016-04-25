class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        size = len(s)
        if not s or size < 10:
            return []

        ht = {}

        for i in range(size - 9):
            tmp = s[i:i+10]
            ht.setdefault(tmp, 0)
            ht[tmp] += 1

        ans = []

        for (k, v) in ht.items():
            if v > 1:
                ans.append(k)
        return ans

s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
print Solution().findRepeatedDnaSequences(s)
