"""
This question need to be solved later
"""

class Solution:
    cache = {}
    # @return a boolean
    def isMatch(self, s, p):
        if (s, p) in self.cache:
            return self.cache[(s, p)]

        if not p:
            return not s

        if len(p) == 1 or p[1] != '*':
            self.cache[(s[1:], p[1:])] = self.isMatch(s[1:], p[1:])
            return len(s) > 0 and (p[0] == '.' or s[0] == p[0]) \
                and self.cache[(s[1:], p[1:])]

        while s and (p[0] == '.' or s[0] == p[0]):
            self.cache[(s, p[2:])] = self.isMatch(s, p[2:])
            if self.cache[(s, p[2:])]:
                return True
            s = s[1:]

        self.cache[(s, p[2:])] = self.isMatch(s, p[2:])
        return self.cache[(s, p[2:])]
