class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        board_row = len(board) # rows
        board_col = len(board[0]) # columns

        def dfs(row, col):
            # if row/col is <> size of board or cell is not O then return
            if row < 0 or col < 0 or row >= board_row or col >= board_col or board[row][col] != 'O':
                return
            
            # set the O cell to U (Uncaptured)
            board[row][col] = 'U'
            
            dfs(row, col-1) # left
            dfs(row, col+1) # right
            dfs(row-1, col) # top
            dfs(row+1, col) # bottom
        
        # 1st iteration -> only borders -> marl all O on boarder cells as U
        for row in range(board_row):
            for col in range(board_col):
                if ((row in [0, board_row - 1]) or (col in [0, board_col - 1])) and board[row][col] == 'O':
                    dfs(row, col)
        
        # 2nd iteration -> non-border cells -> mark all O as X (means captured)
        for row in range(1, board_row-1):
            for col in range(1, board_col-1):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        
        # 3rd iteration -> all cells -> revert U cells to O, i.e. border O cells
        for row in range(board_row):
            for col in range(board_col):
                if board[row][col] == 'U':
                    board[row][col] = 'O'
