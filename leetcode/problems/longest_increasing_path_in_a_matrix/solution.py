class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        maxPath = -1

        def dfs(row, col, prev):
            if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] <= prev:
                return 0
            
            if not dp[row][col]:
                dp[row][col] = 1 + max(
                    dfs(row - 1, col, matrix[row][col]),
                    dfs(row + 1, col, matrix[row][col]),
                    dfs(row, col - 1, matrix[row][col]),
                    dfs(row, col + 1, matrix[row][col])
                )

            return dp[row][col]

        
        for row in range(rows):
            for col in range(cols):
                curPath = dfs(row, col, -1)
                maxPath = max(maxPath, curPath)
        
        return maxPath