class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for row in range(rows):
            for col in range(cols):
                ones = 0
                for x, y in directions:
                    nx, ny = row + x, col + y
                    if 0 <= nx < rows and 0 <= ny < cols and abs(board[nx][ny]) == 1:
                        ones += 1
                
                if board[row][col] == 1 and (ones < 2 or ones > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and ones == 3:
                    board[row][col] = 2
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0