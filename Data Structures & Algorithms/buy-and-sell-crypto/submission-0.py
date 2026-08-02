class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_val = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            sell_val = prices[i]
            if (sell_val - min_buy_val) > max_profit:
                max_profit = sell_val - min_buy_val
            
            if sell_val < min_buy_val:
                min_buy_val = sell_val
        
        return max_profit
