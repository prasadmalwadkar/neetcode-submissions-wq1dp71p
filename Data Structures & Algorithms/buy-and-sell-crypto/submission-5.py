class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r =0,0
        profit = 0
        if not prices:
            return 0
        left,right = prices[l], prices[r]
        while r<len(prices):
            if prices[l]>prices[r]:
                l=r
            else:
                profit = max(profit, prices[r]-prices[l])
                r+=1

        return profit

        