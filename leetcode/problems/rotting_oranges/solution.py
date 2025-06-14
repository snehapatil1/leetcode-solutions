class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        rotten = deque()
        minutes = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    rotten.append((row, col))
        
        while rotten and fresh > 0:
            minutes += 1
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nrow, ncol = row + dr, col + dc
                    if nrow < 0 or nrow >= rows or ncol < 0 or ncol >= cols:
                        continue
                    if grid[nrow][ncol] == 0 or grid[nrow][ncol] == 2:
                        continue
                    
                    fresh -= 1
                    grid[nrow][ncol] = 2
                    rotten.append((nrow, ncol))
        
        return minutes if fresh == 0 else -1