class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # ROWS, COLS = len(matrix), len(matrix[0])
        # transposeMatrix = [[None] * ROWS for _ in range(COLS)]
        
        # for row in range(ROWS):
        #     for col in range(COLS):
        #         transposeMatrix[col][row] = matrix[row][col]
        
        # return transposeMatrix

        return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]