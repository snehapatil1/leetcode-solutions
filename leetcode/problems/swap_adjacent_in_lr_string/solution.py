class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # R can only move to right
        # L can only move to L
        # X can be considered as void spaces

        start_moves, end_moves = [], []
        start_moves_index, end_moves_index = [], []

        # if it is not a void space means we can move this L/R so store the move and it's index
        # do this for both start and end
        for i in range(len(start)):
            if start[i] != 'X':
                start_moves.append(start[i])
                start_moves_index.append(i)
            if end[i] != 'X':
                end_moves.append(end[i])
                end_moves_index.append(i)
        
        # if in the start and end moves list following conditions aren't met then return False
        # 1. number of total moves
        # 2. sequence of each move
        if start_moves != end_moves:
            return False

        for j in range(len(start_moves)):
            # if current move is R then it can only move to right which means in start the index of R will be < than it's index in end, if not then return False
            if start_moves[j] == 'R' and start_moves_index[j] > end_moves_index[j]:
                return False
            # if current move is L then it can only move to the left which means in start the index of L will be > than it's index in end, if not then return False
            if start_moves[j] == 'L' and start_moves_index[j] < end_moves_index[j]:
                return False
        
        return True