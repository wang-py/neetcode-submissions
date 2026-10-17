class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        for i in range(1, len(prices)):
            profit.append(prices[i] - min(prices[0:i]))
            
        if profit:
            max_profit = max(profit)
        else:
            max_profit = 0
        
        if max_profit < 0:
            max_profit = 0

        return max_profit