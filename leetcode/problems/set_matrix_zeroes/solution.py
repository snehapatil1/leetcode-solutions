class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        is_col = False
        for row in range(rows):
            if matrix[row][0] == 0:
                is_col = True
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        
        for row in range(1, rows):
            for col in range(1, cols):
                if not matrix[0][col] or not matrix[row][0]:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for col in range(cols):
                matrix[0][col] = 0
        
        if is_col:
            for row in range(rows):
                matrix[row][0] = 0