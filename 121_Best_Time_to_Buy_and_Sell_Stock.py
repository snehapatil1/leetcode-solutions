"""
    Data Structures: Array, Hash Table
    Time Complexity: O(n)
    Space Complexity: O(n)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = prices[0]

        for i in range(len(prices)):
            profit = max(prices[i]-min_buy, profit)
            min_buy = min(prices[i], min_buy)
        
        return profit
