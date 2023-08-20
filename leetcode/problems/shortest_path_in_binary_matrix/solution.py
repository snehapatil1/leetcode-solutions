class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid) - 1, len(grid[0]) - 1
        if grid[0][0] != 0 or grid[rows][cols] != 0:
            return -1
        
        min_path = 1
        visited = set((0, 0))
        queue = collections.deque([(0, 0, 1)])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, 1], [1, -1]]

        while queue:
            r_cell, c_cell, minpath = queue.popleft()
            if r_cell == rows and c_cell == cols:
                return minpath
            for r, c in directions:
                if (0 <= (r_cell + r) <= rows) and (0 <= (c_cell + c) <= cols) and (grid[r_cell + r][c_cell + c] == 0) and ((r_cell + r, c_cell + c) not in visited):
                    queue.append((r_cell + r, c_cell + c, minpath + 1))
                    visited.add((r_cell + r, c_cell + c))
        
        return -1