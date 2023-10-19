class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[float('inf')] * (i + 1) for i in range(n)]

        for col in range(n):
            dp[n - 1][col] = triangle[n - 1][col]

        for row in range(n - 2, -1, -1):
            for col in range(row + 1):
                if 0 <= row < n and 0 <= col < (row + 1):
                    nrow = row if row + 1 > n else row + 1
                    ncol = col if col + 1 > row + 1 else col + 1
                    val = min(dp[nrow][col], dp[nrow][ncol])
                    dp[row][col] = triangle[row][col] + (0 if val == float('inf') else val)
        
        return dp[0][0]