# http://bookshadow.com/weblog/2015/08/06/leetcode-candy/

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        size = len(ratings)
        candies = [1] * size

        for i in range(1, size):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(size-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1] + 1, candies[i])
        return sum(candies)


ratings = [2,2,5,3,2]
print Solution().candy(ratings)
