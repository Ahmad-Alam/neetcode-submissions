class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 100
        sell = 0
        profit = 0

        for i in range(len(prices)-1):
            if buy > prices[i]:
                buy = prices[i]
                sell = prices[i+1]
            elif sell < prices[i+1]:
                sell = prices[i+1]
            
            if profit < (sell - buy):
                profit = sell - buy
        
        
        if profit < 0:
            profit = 0

        return profit