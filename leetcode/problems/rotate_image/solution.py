class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l, r = 0, len(matrix) - 1
        while l < r:
            top, bottom = l, r
            for i in range(r - l):
                topLeft = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1



        # n = len(matrix[0])
        # for i in range(n // 2 + n % 2):
        #     for j in range(n // 2):
        #         temp = matrix[n - 1 - j][i]
        #         matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
        #         matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
        #         matrix[j][n - 1 - i] = matrix[i][j]
        #         matrix[i][j] = temp
