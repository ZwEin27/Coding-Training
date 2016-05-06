class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if not m:
            return
        n = len(board[0])


        neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in range(m):
            for j in range(n):
                val = board[i][j]
                live_count = 0
                # print 'i, j: ', i, j
                for neighbor_offset in neighbor_offsets:
                    r = i + neighbor_offset[0]
                    c = j + neighbor_offset[1]
                    if r >= 0 and r < m and c >= 0 and c < n:
                        # print 'r, c: ', r, c
                        nei_val = board[r][c]
                        if nei_val == 1 or nei_val == -1:
                            live_count += 1

                if live_count == 3 and val == 0:
                    board[i][j] = -2
                elif (live_count < 2 or live_count > 3) and val == 1:
                    board[i][j] = -1

                # print live_count, board[i][j]
        # print board
        for i in range(m):
            for j in range(n): 
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == -2:
                    board[i][j] = 1
                


board = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
Solution().gameOfLife(board)
print board
