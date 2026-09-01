class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_profit = 0
        min_buy = prices[0]

        while i < len(prices):
            sell = prices[i]
            min_buy = min(min_buy, prices[i])
            max_profit = max(sell - min_buy, max_profit)
            i += 1
        return max_profit