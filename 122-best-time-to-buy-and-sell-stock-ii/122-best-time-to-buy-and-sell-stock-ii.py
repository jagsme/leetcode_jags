class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            returns = prices[i+1] - prices[i]
            if returns > 0:
                profit = returns + profit
    
        return profit