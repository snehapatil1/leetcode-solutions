class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            
            if grid[row][col] == 1:
                return True
            
            grid[row][col] = 1
            left = dfs(row, col - 1)
            right = dfs(row, col + 1)
            up = dfs(row - 1, col)
            down = dfs(row + 1, col)
            return left and right and up and down
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and dfs(row, col):
                    count += 1
        
        return count