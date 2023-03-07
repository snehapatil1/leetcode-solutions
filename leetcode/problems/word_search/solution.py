class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        
        def dfs(i, j, curr):
            if curr == len(word):
                return True
            
            if i < 0 or j >= cols or j < 0 or i >= rows or board[i][j] != word[curr] or (i, j) in visited:
                return False
            
            visited.add((i, j))
            res = dfs(i + 1, j, curr + 1) or dfs(i - 1, j, curr + 1) or dfs(i, j + 1, curr + 1) or dfs(i, j - 1, curr + 1)
            visited.remove((i, j))
            return res
            
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False