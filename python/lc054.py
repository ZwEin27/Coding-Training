# https://leetcode.com/discuss/95784/very-easy-to-understand-python-solution
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        res = []
        m, n = len(matrix), len(matrix[0])
        i, j, mi, mj = 0, 0, 0, 1
        for _ in range(m*n):
            res.append(matrix[i][j])
            matrix[i][j] = -1
            if matrix[(i+mi)%m][(j+mj)%n] == -1:
                mi, mj = mj, -mi
            i += mi
            j += mj
        return res





matrix = [[1,2,3],[4,5,6],[7,8,9]]
print Solution().spiralOrder(matrix)
