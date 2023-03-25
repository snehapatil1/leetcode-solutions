class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                matrix[row][col] = int(matrix[row][col])
                if matrix[row][col] and row > 0 and col > 0:
                    matrix[row][col] = min(matrix[row - 1][col], matrix[row - 1][col - 1], matrix[row][col - 1]) + 1
        return len(matrix) and max(map(max, matrix)) ** 2