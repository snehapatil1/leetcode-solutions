class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # [1, 1, 1]
        # [0, 1, 2]
        # [0, 1, 3]

        count = 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]
        
        
        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] == 1:
                    continue
                
                if row == 0 and col == 0:
                    dp[row][col] = 1
                elif row == 0 and col > 0:
                    dp[row][col] = max(dp[row][col], dp[row][col - 1])
                elif row > 0 and col == 0:
                    dp[row][col] = max(dp[row][col], dp[row - 1][col])
                else:
                    dp[row][col] = max(dp[row][col], (dp[row - 1][col] + dp[row][col - 1]))
        
        return dp[rows - 1][cols - 1]