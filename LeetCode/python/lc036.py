class Solution:

    def __init__(self):  
        self.row_temp = [0]*10;
        self.col_temp = [[0 for col in range(10)] for row in range(10)];
        self.sub_temp = [[0 for col in range(10)] for row in range(10)];

    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        self.row_temp[8] = 1;
        for i in range(0, 9):
            self.row_temp = [0]*10;
            for j in range(0, 9):
                cur = board[i][j];
                if cur != '.':
                    if (not self.checkValid(self.row_temp, cur)) or    \
                        (not self.checkValid(self.col_temp[j], cur)) or    \
                        (not self.checkValid(self.sub_temp[i - i%3 + j/3], cur)):
                            return False;
        return True;
                    


    def checkValid(self, temp, data):
        val = int(data);
        if temp[val] == 1:
            return False;
        else:
            temp[val] = 1;
            return True;


