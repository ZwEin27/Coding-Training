class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        min_price_idx = 0
        max_profit = 0
        for i in range(size):
            if prices[i] < prices[min_price_idx]:
                min_price_idx = i
            profit = prices[i] - prices[min_price_idx]
            if profit > max_profit:
                max_profit = profit

        return max_profit


