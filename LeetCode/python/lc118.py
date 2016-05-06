class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return [];
        # elif numRows == 1:
        #     return [1];
        # elif numRows == 2:
        #     return [1, 1];
        # else:

        row = [];
        result = [];
        for i in range(0, numRows):
            row = self.pt(row);
            result.append(row);
        return result;
    
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
