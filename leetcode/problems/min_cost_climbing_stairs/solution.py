class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) + 1
        if n <= 1:
            return 0
        
        dp = [0] * n

        for idx in range(2, n):
            dp[idx] = min(cost[idx - 1] + dp[idx - 1], cost[idx - 2] + dp[idx - 2])
        
        return dp[-1]