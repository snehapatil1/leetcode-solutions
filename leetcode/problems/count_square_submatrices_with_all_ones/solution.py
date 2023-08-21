class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        @cache
        def update_square_count(row, col):
            if matrix[row][col] == 1:
                if row != 0 and col != 0:
                    return min(update_square_count(row, col - 1), update_square_count(row - 1, col - 1), update_square_count(row - 1, col)) + 1
                else:
                    return 1
            else:
                return 0
            
        return sum(update_square_count(row, col) for row in range(rows) for col in range(cols))