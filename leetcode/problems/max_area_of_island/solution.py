class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def dfs(row, col, area):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or grid[row][col] != 1:
                return 0
            
            visited.add((row, col))
            area = 1 + dfs(row + 1, col, area) + dfs(row - 1, col, area) + dfs(row, col + 1, area) + dfs(row, col - 1, area)

            return area
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = dfs(row, col, 0)
                    maxArea = max(maxArea, area)
        
        return maxArea