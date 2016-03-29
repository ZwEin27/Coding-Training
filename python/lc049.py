# https://leetcode.com/problems/anagrams/
# begin for problem



class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()


strs = ["tea","and","ate","eat","den"]
print Solution().groupAnagrams(strs)