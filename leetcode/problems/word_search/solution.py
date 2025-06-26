class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        
        def dfs(row, col, curr):
            if curr == len(word):
                return True
            
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or board[row][col] != word[curr]:
                return False

            visited.add((row, col))
            res = dfs(row - 1,  col, curr + 1) or dfs(row + 1,  col, curr + 1) or dfs(row,  col - 1, curr + 1) or dfs(row,  col + 1, curr + 1)
            visited.remove((row, col))
            
            return res

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False