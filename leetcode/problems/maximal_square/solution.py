class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0]*(cols) for _ in range(rows)]
        max_side = 0

        for row in range(rows):
            for col in range(cols):
                cell = int(matrix[row][col])
                if not cell:
                    continue
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = min(dp[row][col - 1], dp[row - 1][col - 1], dp[row - 1][col]) + 1
                max_side = max(max_side, dp[row][col])
        
        return max_side ** 2