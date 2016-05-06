class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # print ord('a')
        
        # word to bitmap
        bitmap_list = []
        for word in words:
            bitmap = 0
            for ch in word:
                offset = ord(ch) - ord('a')
                bitmap |= 1 << offset
            bitmap_list.append(bitmap)

        best = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if bitmap_list[i]&bitmap_list[j] == 0:
                    length = len(words[i]) * len(words[j])
                    if length > best:
                        best = length
        return best
        


print Solution().maxProduct(["a", "aa", "aaa", "aaaa"])