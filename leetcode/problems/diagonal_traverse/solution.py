class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        rows, cols = len(mat), len(mat[0])
        output = []
        up = 1
        row, col = 0, 0
        
        while row < rows and col < cols:
            output.append(mat[row][col])
            nrow = row + (-1 if up == 1 else 1)
            ncol = col + (1 if up == 1 else -1)
            if nrow < 0 or nrow == rows or ncol < 0 or ncol == cols:
                if up:
                    row += (col == cols - 1)
                    col += (col < cols - 1)
                else:
                    col += (row == rows - 1)
                    row += (row < rows - 1)
                up = 1 - up
            else:
                row = nrow
                col = ncol
        
        return output
