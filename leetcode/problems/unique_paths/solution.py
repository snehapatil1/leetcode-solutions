class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                board[row][col] = board[row - 1][col] + board[row][col - 1]
        
        return board[m - 1][n - 1]