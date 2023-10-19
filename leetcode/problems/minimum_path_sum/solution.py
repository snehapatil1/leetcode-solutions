class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[float('inf')] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if 0 <= row < rows and 0 <= col < cols:
                    prevVal = min(dp[max(row - 1, 0)][col], dp[row][max(col - 1, 0)])
                    dp[row][col] = (grid[row][col] + (0 if prevVal == float('inf') else prevVal))
        
        return dp[rows - 1][cols - 1]