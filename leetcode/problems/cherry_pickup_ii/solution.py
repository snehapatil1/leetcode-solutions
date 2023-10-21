class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[[0] * cols for _ in range(cols)] for _ in range(rows)]

        for row in reversed(range(rows)):
            for r1 in range(cols):
                for r2 in range(cols):
                    result = grid[row][r1] if r1 == r2 else grid[row][r1] + grid[row][r2]
                    if row != rows - 1:
                        maxval = 0
                        for col1 in [r1 - 1, r1, r1 + 1]:
                            for col2 in [r2 - 1, r2, r2 + 1]:
                                if 0 <= col1 < cols and 0 <= col2 < cols:
                                    maxval = max(maxval, dp[row + 1][col1][col2])
                        result += maxval
                    
                    dp[row][r1][r2] = result
        
        return dp[0][0][cols - 1]