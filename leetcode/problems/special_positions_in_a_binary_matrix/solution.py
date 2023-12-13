class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        nRow = [0] * ROWS
        nCol = [0] * COLS
        cnt = 0

        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 1:
                    nRow[row] += 1
                    nCol[col] += 1
        
        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 1:
                    if nRow[row] == 1 and nCol[col] == 1:
                        cnt += 1
        
        return cnt