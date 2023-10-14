class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for c, t in zip(cost, time):
            for j in range(n , -1, -1):
                dp[j] = min(dp[j], dp[max(j - t - 1, 0)] + c)
        
        return dp[n]