class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if len(haystack) == 0 and len(needle) == 0:
            return 0;
        elif len(haystack) != 0 and len(needle) == 0:
            return 0;
        elif len(haystack) == 0 and len(needle) != 0:
            return -1;

        span = len(needle) - 1;
        idx_prev = 0;
        idx_next = idx_prev + span;
        for i in range(0, len(haystack)):
            if idx_next >= len(haystack):
                return -1;
            if haystack[idx_prev] == needle[0]:
                for j in range(0, len(needle)):
                    if haystack[idx_prev + j] != needle[j]:
                        break;
                    if j == len(needle) - 1:
                        return idx_prev;

            idx_prev += 1;
            idx_next += 1;

        return -1;

        # idx = 0;
        # start = -1;
        # for i in range(0, len(haystack)):
        #     if haystack[i] == needle[idx]:
        #         if start == -1:
        #             start = i;
        #         idx += 1;
        #     else:
        #         idx = 0;
        #         start = -1;
        #     if idx == len(needle):
        #         return start;
        # return -1;