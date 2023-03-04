class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()
        matrix_rows = len(matrix)
        matrix_cols = len(matrix[0])

        # if given cell is 0 then add that row and col in above set to mark those entire rows and cols as 0
        for row in range(matrix_rows):
            for col in range(matrix_cols):
                if matrix[row][col] == 0:
                    rows.add(row)
                    columns.add(col)
        
        # mark all those rows as 0
        for each_row in rows:
            for col in range(matrix_cols):
                matrix[each_row][col] = 0
        
        # mark all those columns as 0
        for each_col in columns:
            for row in range(matrix_rows):
                matrix[row][each_col] = 0