class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        matrix = [[-1 for _ in range(3)] for _ in range(3)]
        rows, cols = 3, 3
        for idx in range(len(moves)):
            row, col = moves[idx][0], moves[idx][1]
            if idx % 2:
                # player B
                matrix[row][col] = 'O'
            else:
                # player A
                matrix[row][col] = 'X'
        
        def row_won(player):
            for row in range(rows):
                if matrix[row][0] == matrix[row][1] == matrix[row][2] == player:
                    return True
        
        def col_won(player):
            for col in range(cols):
                if matrix[0][col] == matrix[1][col] == matrix[2][col] == player:
                    return True
        
        def diagonal_won(player):
            if (
                matrix[0][0] == matrix[1][1] == matrix[2][2] == player \
                or  matrix[0][2] == matrix[1][1] == matrix[2][0] == player
            ):
                return True
        
        def does_player_win(player):
            return row_won(player) or col_won(player) or diagonal_won(player)

        # player A wins
        if does_player_win('X'):
            return 'A'
        
        # player B wins
        if does_player_win('O'):
            return 'B'
        
        if -1 in [matrix[row][col] for row in range(rows) for col in range(cols)]:
            # Draw - no one wins and moves left
            return 'Pending'
        else:
            # Pending - no one wins and no moves left
            return 'Draw'