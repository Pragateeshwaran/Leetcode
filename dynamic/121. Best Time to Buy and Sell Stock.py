class Solution:
   def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        maxProfit = 0
        minPurchase = prices[0]
        for i in range(1, len(prices)):		
            maxProfit = max(maxProfit, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
        return maxProfit

print(Solution().maxProfit(prices = [7,1,5,3,6,4]))