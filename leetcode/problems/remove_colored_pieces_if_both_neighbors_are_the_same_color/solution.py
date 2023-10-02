class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        if n < 3:
            return False
        
        aliceMoves, bobMoves = 0, 0

        for idx in range(2, n):
            if colors[idx - 2] == colors[idx - 1] == colors[idx] == 'A':
                aliceMoves += 1
            if colors[idx - 2] == colors[idx - 1] == colors[idx] == 'B':
                bobMoves += 1
        
        return aliceMoves - bobMoves >= 1