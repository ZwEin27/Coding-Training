class Solution:
    def strStr(self, source, target):
        if source == None or target == None:
            return -1
        slen = len(source)
        tlen = len(target)
        for i in range(0, slen - tlen + 1):
            j = 0
            while j < tlen:
                if source[i+j] != target[j]:
                    break
                j += 1
            if j == tlen:
                return i
        return -1
        
# class Solution:
#     def strStr(self, source, target):
#         # write your code here
#         if source == None or target == None:
#             return -1
#         slen = len(source)
#         tlen = len(target)
#         if slen < tlen:
#             return -1
#
#         for i in range(slen-tlen+1):
#             if source[i:i+tlen] == target:
#                 return i
#         return -1
