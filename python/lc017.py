class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = [" ", "", ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        dlen = len(digits)
        result = []
        if dlen > 0:
            letter_arr = letters[int(digits[0])]
            if dlen == 1:
                return letter_arr
            else:
                tmp = self.letterCombinations(digits[1:])
                len1 = len(letter_arr)
                len2 = len(tmp)
                for i in range(len1):
                    for j in range(len2):
                        result.append(letter_arr[i] + tmp[j]);
                


        return result 




