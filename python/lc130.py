class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        r_size = len(board)
        queue = []
        
        if r_size > 0:
            c_size = len(board[0])
            surround_nodes = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited = [[False] * c_size for x in range(r_size)]
            # print visited
    
    
            for i in range(r_size):
                for j in range(c_size):
                    if not visited[i][j] and board[i][j] == 'O':
                        queue.append(i*c_size + j)
                        visited_nodes = []
                        surround = True
                        visited[i][j] = True
                        while len(queue) > 0:
                            node = queue.pop(0)
                            # print 'node: ' + str(node)
                            r = node/c_size
                            c = node%c_size
                            
                            visited_nodes.append(node)
                            
                            for sn in surround_nodes:
                                sn_ridx = r + sn[0]
                                sn_cidx = c + sn[1]

                                if sn_ridx >= 0 and sn_cidx >= 0 and sn_ridx < r_size and sn_cidx < c_size:
                                    # print (sn_ridx, sn_cidx)
                                    if board[sn_ridx][sn_cidx] == 'O' and not visited[sn_ridx][sn_cidx]:
                                        queue.append(sn_ridx*c_size + sn_cidx)
                                    visited[sn_ridx][sn_cidx] = True

                                else:
                                    surround = False

                            
                                
                        
                        # print visited_nodes
                        # print visited
                        if surround:
                            # print 'node' + str((i,j) )
                            # print visited_nodes
                            for vnode in visited_nodes:
                                r = vnode/c_size
                                c = vnode%c_size
                                tmp = list(board[r])
                                tmp[c] = 'X'
                                board[r] = ''.join(tmp)

        

    """
    def isSurrounded(i, board):
        size = len(board)
        r = i/size
        c = i%size
        if r == 0 or c == 0:
            return False
        if r == size - 1 or c == size - 1:
            return False
        if board[r+1][c] == 'X' and board[r-1][c] == 'X' and board[r][c+1] == 'X' and board[r][c-1] == 'X':
            return False
        return True
    """

# board = [
#             ['X', 'X', 'X', 'X'],
#             ['X', 'O', 'O', 'X'],
#             ['X', 'X', 'O', 'X'],
#             ['X', 'O', 'X', 'X']
#         ]

# board = ["XXX","XOX","XXX"]

board = ["O"]

# board = [
#             "XOOXXXOXOO",
#             "XOXXXXXXXX",
#             "XXXXOXXXXX",
#             "XOXXXOXXXO",
#             "OXXXOXOXOX",
#             "XXOXXOOXXX",
#             "OXXOOXOXXO",
#             "OXXXXXOXXX",
#             "XOOXXOXXOO",
#             "XXXOOXOXXO"
#         ]

Solution().solve(board)

print board
