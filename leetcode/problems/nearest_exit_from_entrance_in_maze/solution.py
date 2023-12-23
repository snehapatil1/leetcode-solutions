from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([(entrance[0], entrance[1], 0)])
        ROWS, COLS = len(maze), len(maze[0])

        visited = set()
        while queue:
            newQueue = []
            for cell in queue:
                row, col, steps = cell[0], cell[1], cell[2]
                if (row, col) != (entrance[0], entrance[1]) and (row in (0, ROWS - 1) or col in (0, COLS - 1)):
                    return steps
                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nrow, ncol = row + x, col + y
                    if 0 <= nrow < ROWS and 0 <= ncol < COLS and maze[nrow][ncol] == '.' and (nrow, ncol) not in visited:
                        newQueue.append((nrow, ncol, steps + 1))
                        visited.add((nrow, ncol))
            queue = newQueue
        
        return -1