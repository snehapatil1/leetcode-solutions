class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def traverse(row, col, area):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or grid[row][col] != 1:
                return 0
            
            visited.add((row, col))
            area = 1 + traverse(row - 1, col, area) + traverse(row + 1, col, area) + traverse(row, col - 1, area) + traverse(row, col + 1, area)
            
            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = traverse(row, col, 0)
                    max_area = max(max_area, area)

        return max_area