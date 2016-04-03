# http://www.tuicool.com/articles/i22yam

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row_size = len(triangle)

        for r in range(row_size-2, -1, -1):
            for c in range(0, r+1):
                if triangle[r+1][c] < triangle[r+1][c+1]:
                    triangle[r][c] += triangle[r+1][c]
                else:
                    triangle[r][c] += triangle[r+1][c+1]
        return triangle[0][0]


        # dp = [0]*row_size
        # ans = triangle[0][0]
        # for i in range(1, row_size):
        #     idx = dp[i-1]

        #     if triangle[i][idx] < triangle[i][idx+1]:
        #         min_idx = idx
        #     else:
        #         min_idx = idx + 1
        #     print idx, min_idx, triangle[i][idx] < triangle[i][idx+1], triangle[i][min_idx]
        #     ans += triangle[i][min_idx]
        # return ans

triangle = [[-1],[2,3],[1,-1,-3]]
print Solution().minimumTotal(triangle)