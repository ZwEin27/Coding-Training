# http://bookshadow.com/weblog/2015/11/24/leetcode-best-time-to-buy-and-sell-stock-with-cooldown/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        days = len(prices)
        sells = [None]*days
        buys = [None]*days
        sells[0] = 0
        buys[0] = -prices[0]

        for di in range(1, days):
            gap = prices[di] - prices[di-1]
            sells[di] = max(buys[di-1]+prices[di], sells[di-1]+gap)
            # buys[di] = max(sells[di-2]-prices[di] if di > 1 else 0, buys[di-1]-gap)
            buys[di] = max(buys[di - 1] - gap, \
                          sells[di - 2] - prices[di] if di > 1 else None)

        print sells
        print buys
        return max(sells)




prices = [1, 2, 3, 0, 2]
print Solution().maxProfit(prices)
