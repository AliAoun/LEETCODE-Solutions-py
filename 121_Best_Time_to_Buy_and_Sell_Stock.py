class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                cMax = prices[r] - prices[l]
                res = max(cMax, res)    
            else:
                l = r
            r += 1
            
        return res