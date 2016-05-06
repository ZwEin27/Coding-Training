class Solution(object):

    def __init__(self):
        self.neighbor_idx = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # row_size = len(board)
        # if row_size > 0:
        #     col_size = len(board[0])
        
        hm = {}
        for w in word:
            hm.setdefault(w, 0)
            hm[w] += 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                w = board[i][j]
                if hm.has_key(w):
                    hm[w] -= 1

        for (k, v) in hm.items():
            if v > 0:
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                start = (i, j)
                visited = [start]
                if self.check(board, word, start, visited):
                    return True
        return False
                

    def check(self, board, word, start, visited):
        # print word, str(start)
        # if len(word) == 0:
        #     return False

        ri = start[0]
        ci = start[1]
        cur = board[ri][ci]
        target = word[0]
        row_size = len(board)
        # if row_size != 0:
        col_size = len(board[0])
        # else:
        #     col_size = 0

        if cur == target:
            if len(word) == 1:
                return True
            
            for nei_idx in self.neighbor_idx:
                idx = (start[0]+nei_idx[0], start[1]+nei_idx[1])
                nri = idx[0]
                nci = idx[1]
                if nri >=0 and nri < row_size and nci >=0 and nci < col_size:
                    if idx not in visited:
                        v2 = list(visited)
                        v2.append(idx)
                        if self.check(board, word[1:], idx, v2):
                            return True
        return False


board = [
            "aaa",
            "abb",
            "abb",
            "bbb",
            "bbb",
            "aaa",
            "bbb",
            "abb",
            "aab",
            "aba"
        ]

word = "aabaaaabbb"
print Solution().exist(board, word)

        
