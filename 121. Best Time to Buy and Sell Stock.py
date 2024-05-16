class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, max1 = 0, 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                max1 = max(max1, prices[r]-prices[l])
        return max1