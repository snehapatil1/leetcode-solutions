class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def create_board():
            self.grid = [['' for _ in range(3)] for _ in range(3)]
            self.x_count, self.o_count = 0, 0

            for row in range(len(board)):
                for col in range(len(board[0])):
                    self.grid[row][col] = board[row][col]
                    if board[row][col] == 'X':
                        self.x_count += 1
                    if board[row][col] == 'O':
                        self.o_count += 1

        def valid_row(player):
            for row in range(len(self.grid)):
                if self.grid[row][0] == player and self.grid[row][1] == player and self.grid[row][2] == player:
                    return True
            
            return False
        
        def valid_column(player):
            for col in range(len(self.grid[0])):
                if (self.grid[0][col] == player and self.grid[1][col] == player and self.grid[2][col] == player):
                    return True
            
            return False
        
        def valid_diagonal(player):
            if (
                (self.grid[0][0] == player and self.grid[1][1] == player and self.grid[2][2] == player) \
                or (self.grid[0][2] == player and self.grid[1][1] == player and self.grid[2][0] == player)
            ):
                return True
            
            return False
        
        def winner(player):
            if valid_row(player): return True
            if valid_column(player): return True
            if valid_diagonal(player): return True
            
            return False

        def game_board_validation():
            # if len O > len X : False
            if self.o_count > self.x_count: return False

            # if len X > len O + 1 : False
            if self.x_count > self.o_count + 1: return False
            
            # if both X and O wins : False
            if winner('X') and winner('O'): return False

            # if X wins and len X == len O : False 
            if winner('X') and self.x_count == self.o_count: return False
            
            # if O wins and len X > len O : False
            if winner('O') and self.x_count > self.o_count: return False

            return True

        create_board()
        return game_board_validation()