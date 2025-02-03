class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minSoFar = float('inf')
        for price in prices:
            minSoFar = min(minSoFar, price)
            profit = max(profit, price - minSoFar)

        return profit