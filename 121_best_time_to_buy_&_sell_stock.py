class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices[0]
        for p in prices[1:]:
            if p < min_price:
                min_price = p
            elif max_profit < p - min_price:
                max_profit = p - min_price
        return max_profit
        