class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        m = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                m = max(profit, m)
        
        return m