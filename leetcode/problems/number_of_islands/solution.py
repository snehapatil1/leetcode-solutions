class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        
        def traverse(row, col):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
                grid[row][col] = 'V'

                traverse(row - 1, col)
                traverse(row + 1, col)
                traverse(row, col - 1)
                traverse(row, col + 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    traverse(row, col)

        return islands