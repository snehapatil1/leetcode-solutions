class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        for row in range(1, rows):
            for col in range(cols):
                matrix[row][col] += min(matrix[row - 1][max(0, col - 1)], matrix[row - 1][col], matrix[row - 1][min(cols - 1, col + 1)])
        
        return min(matrix[rows - 1])

        # pathSum = [[float('inf')] * cols for _ in range(rows)]
        # queue = deque()

        # for col in range(cols):
        #     pathSum[0][col] = 0
        #     queue.append((0, col))
        
        # while queue:
        #     r, c = queue.popleft()
        #     pathSum[r][c] += matrix[r][c]
        #     for nrow, ncol in [(r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]:
        #         if 0 <= nrow < rows and 0 <= ncol < cols:
        #             if pathSum[nrow][ncol] == float('inf'):
        #                 pathSum[nrow][ncol] = pathSum[r][c]
        #                 queue.append((nrow, ncol))
        #             else:
        #                 pathSum[nrow][ncol] = min(pathSum[nrow][ncol], pathSum[r][c])
        # return min(pathSum[rows - 1])