class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        dp = [0] * (n + 1)
        prevColor = 'a'
        prevTime = 0

        for idx in range(1, n + 1):
            if colors[idx - 1] == prevColor:
                dp[idx] = dp[idx - 1] + min(neededTime[idx - 1], prevTime)
                prevTime = max(prevTime, neededTime[idx - 1])
            else:
                dp[idx] = dp[idx - 1]
                prevColor = colors[idx - 1]
                prevTime = neededTime[idx - 1]
        
        return dp[n]