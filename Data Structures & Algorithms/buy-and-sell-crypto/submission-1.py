class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mmin = max(prices)
        res = 0
        for price in prices:
            mmin = min(price, mmin)
            res = max(res, price - mmin)
        
        return res