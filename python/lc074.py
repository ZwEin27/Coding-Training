class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        start = 0
        end = len(matrix) - 1
        return self.searchRow(matrix, 0, len(matrix) - 1, target)


    def searchRow(self, matrix, start, end, target):
        print start, end
        if start == end:
            row = matrix[start]
            print row
            if row[0] <= target and target <= row[-1]:
                return self.searchTarget(row, 0, len(row)-1, target)
            return False

        mid = (start + end) / 2
        if mid < start or mid > end:
            return False

        if matrix[mid][0] <= target and target <= matrix[mid][-1]:
            row = matrix[mid]
            return self.searchTarget(row, 0, len(row)-1, target)
        if target < matrix[mid][0]:
            return self.searchRow(matrix, start, mid-1, target)
        if matrix[mid][0] < target:
            return self.searchRow(matrix, mid+1, end, target)
        return False

    def searchTarget(self, row, start, end, target):
        print start, end, row
        if start == end:
            if row[start] == target:
                return True
            else:
                return False

        mid = (start + end) / 2
        if mid < start or mid > end:
            return False

        if row[mid] == target:
            return True
        if target < row[mid]:
            return self.searchTarget(row, start, mid-1, target)
        if row[mid] < target:
            return self.searchTarget(row, mid+1, end, target)

        return False

matrix = [[1],[3]]
target = 0

print Solution().searchMatrix(matrix, target)
