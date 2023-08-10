class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(pos, direction, word_idx):
            
            is_boundary = pos[0] < 0 or pos[0] > m-1 or pos[1] < 0 or pos[1] > n-1 or board[pos[0]][pos[1]] == '#'
            
            if word_idx == len(word):
                return is_boundary  
            
            if is_boundary or (board[pos[0]][pos[1]] != ' ' and board[pos[0]][pos[1]] != word[word_idx]):    
                return False

            if not direction:                
                for i, j in move:
                    prev = pos[0] - i, pos[1] - j
                    if 0<=prev[0]<m and 0<=prev[1]<n and board[prev[0]][prev[1]] != '#':
                        continue
                        
                    nxt = pos[0] + i, pos[1] + j                    
                    if dfs(nxt, (i,j), word_idx+1 ):
                        return True         
                    
            else:
                nxt = pos[0] + direction[0], pos[1] + direction[1]
                if dfs(nxt, direction, word_idx + 1):
                    return True   

                
        m = len(board)
        n = len(board[0])
        move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == ' ' or board[i][j] == word[0]:
                    if dfs((i,j), None, 0):
                        return True
                    
        return False