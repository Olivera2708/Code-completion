class Solution:
    def maxProfit(self, prices):
        max = 0
        for i in range(1, len(prices)):
            if prices[i] > max:
                max = prices[i]
        for i in range(1, len(prices)):
            if start < prices[i]: 
                max += prices[i] - start
            start = prices[i]
        return max