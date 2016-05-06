class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1];
        # elif numRows == 1:
        #     return [1];
        # elif numRows == 2:
        #     return [1, 1];
        # else:

        row = [1];
        for i in range(0, rowIndex):
            row = self.pt(row);
        return row;

    def pt(self, row):
        if row == []:
            return [1];
        next_row = [];
        tmp = 0;
        for i in range(0,len(row)):
            next_row.append(tmp + row[i]);
            tmp = row[i];
        next_row.append(1);
        return next_row;