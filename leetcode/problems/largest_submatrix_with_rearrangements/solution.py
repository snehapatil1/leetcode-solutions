class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        output = 0

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]
            
            curr_row = sorted(matrix[row], reverse=True)
            for col in range(cols):
                output = max(output, curr_row[col] * (col + 1))
        
        return output