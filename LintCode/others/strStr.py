class Solution:
    def strStr(self, source, target):
        # write your code here
        if source == None or target == None:
            return -1

        slen = len(source)
        tlen = len(target)
        if slen < tlen:
            return -1

        for i in range(slen-tlen+1):
            if source[i:i+tlen] == target:
                return i


        return -1
