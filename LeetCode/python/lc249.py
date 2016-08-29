class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        ht = {}
        for string in strings:
            ht.setdefault(len(string), [])
            ht[len(string)].append((string, tuple([(ord(c) - ord(string[0])) % 26 for c in string])))



        ans = []
        for (length, tuples) in ht.iteritems():
            inner_ht = {}
            for (string, key) in tuples:
                # print string, key
                inner_ht.setdefault(key, [])
                inner_ht[key].append(string)
            ans += inner_ht.values()
        return ans


                
