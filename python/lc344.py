class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # TLE
        # new_string = ''
        # for i in range(len(s)-1,-1,-1):
        #     new_string += s[i]
        # return new_string

        # TLE
        # s = list(s)
        # size = len(s)
        # cur_idx = size - 1
        #
        # while cur_idx > 0:
        #     target_idx = cur_idx - 1
        #     s.append(s[target_idx])
        #     del s[target_idx]
        #     cur_idx -= 1
        # return ''.join(s)


s = 'hello'
print Solution().reverseString(s)
