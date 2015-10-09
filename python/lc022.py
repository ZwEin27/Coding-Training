class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n > 0:
            self.generate(result, "", n, n)
        return result

    def generate(self, result, str, left, right):
        if left > right:
            return
        if left == 0 and right == 0:
            result.append(str)
        if left > 0:
            self.generate(result, str + "(", left - 1, right)
        if right > 0:
            self.generate(result, str + ")", left, right - 1)











