class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # not in-place version
        # n = len(matrix)

        # result = [[0 for col in range(n)] for row in range(n)]
        # ri = 0
        # rj = 0
        # for j in range(0, n, 1):
        #     for i in range(n-1, -1, -1):
        #         result[ri][rj] = matrix[i][j]
        #         rj += 1
        #         rj %= n
        #     ri += 1
        #     ri %= n
        # matrix = list(result)

        n = len(matrix)
        # fold up and down based on middle line
        for i in range(n/2):
            tmp = matrix[i]
            matrix[i] = matrix[n-1-i]
            matrix[n-1-i] = tmp

        

        # fold based on "\"

        rnd = 0
        while rnd < n:
            idx = rnd + 1
            while idx < n:
                tmp = matrix[rnd][idx]
                matrix[rnd][idx] = matrix[idx][rnd]
                matrix[idx][rnd] = tmp
                idx += 1
            rnd += 1



        # print matrix

    # def swap(self, a, b):
    #     tmp = a
    #     a = b
    #     b = tmp







            