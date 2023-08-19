class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        rows, cols = len(board), len(board[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != 'X':
                return
            
            board[row][col] = 'V'

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'X':
                    dfs(row, col)
                    count += 1
        
        return count