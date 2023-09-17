class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        visited.add((0, 0))
        heap = [(grid[0][0], 0, 0)]
        
        while heap:
            time, row, col = heapq.heappop(heap)
            if row == rows - 1 and col == cols - 1:
                return time
            for x, y in directions:
                nrow, ncol = row + x, col + y
                if 0 <= nrow < rows and 0 <= ncol < cols and (nrow, ncol) not in visited:
                    visited.add((nrow, ncol))
                    heapq.heappush(heap, (max(time, grid[nrow][ncol]), nrow, ncol))
        return -1
        