class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        row_len = len(points)
        col_len = len(points[0])
        # dp = first row
        dp = points[0]
        # max count for each column for 1 row ata time when done from left
        left = [0] * col_len
        # max count for each column for 1 row ata time when done from right
        right = [0] * col_len

        # for each row from 2nd row
        for row in range(1, row_len):
            # for each column from left to right
            for col in range(col_len):
                if col == 0:
                    # if it is 1st column then left[0] will be 1st row 1st col of matrix
                    left[col] = dp[col]
                else:
                    # consider max value of either the cell above current
                    # OR prev cell on left side on same row
                    left[col] = max(left[col - 1] - 1, dp[col])
            
            # for each column from right to left
            for col in range(col_len - 1, -1, -1):
                if col == col_len - 1:
                    # if it is last column then left[last col] will be 1st row last col of matrix
                    right[col] = dp[col]
                else:
                    # consider max value of either the cell above current
                    # OR prev cell on right side on same row
                    right[col] = max(right[col + 1] - 1, dp[col])
            
            for col in range(col_len):
                # for each column on this row, value will be sum of current cell and the max value for that cell from left and right dps
                dp[col] = points[row][col] + max(left[col], right[col])
        
        return max(dp)