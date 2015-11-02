class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        zr = 0
        zc = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zr |= 1 << i
                    zc |= 1 << j

        for i in range(m):
            for j in range(n):
                if (zr & 1 << i) or (zc & 1 << j):
                    # print i,j,'\n'
                    matrix[i][j] = 0

        # print matrix

        # [[0,0,0,5],
        #  [4,3,1,4],
        #  [0,1,1,4],
        #  [1,2,1,3],
        #  [0,0,1,1]]

