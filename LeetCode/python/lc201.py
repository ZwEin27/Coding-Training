class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        m_level = self.get_level(m)
        n_level = self.get_level(n)
        
        if m_level != n_level:
            return 0

        ans = 0
        level = m_level - 1
        while level >= 0 and (m >> level) == (n >> level):

            if m >> level == 1:
                tmp = 1 << level
                ans += tmp
                m &= (tmp - 1)
                n &= (tmp - 1)
            # print ans, level
            level -= 1


        return ans

    def get_level(self, num):
        level = 1
        while 1:
            if num < pow(2, level):
                break
            level += 1
        return level


# m = 0
# n = 2147483647
m = 5
n = 5
print Solution().rangeBitwiseAnd(m, n)