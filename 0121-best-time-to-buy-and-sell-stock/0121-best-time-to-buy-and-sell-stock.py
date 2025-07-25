class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                res = max(res, diff)
            else:
                l = r
        
        return res